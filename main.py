import datetime
import decimal
import pathlib
import argparse
import dataclasses
import typing
import urllib.parse
import requests
import xsdata.formats.dataclass.parsers
import xsdata.formats.dataclass.parsers.config
import xsdata.formats.dataclass.serializers
import xsdata.formats.dataclass.serializers.config
import xsdata.models.datatype
import models.crd
import models.netex

DELIVERY_COMPANY_CODE = "5101"
DB_NETEX_URL = "https://bahnhof.de/daten/netex"
DB_INFRASTRUCTURE_MANAGERS = ("0080", "1080")
IM_COPIED_FIELDS = (
    "url", "postal_address", "accessibility_assessment", "public_use", "covered", "gated", "lighting",
    "all_areas_wheelchair_accessible", "facilities", "site_type", "locale", "private_codes", "info_links",
    "levels", "entrances", "equipment_places", "place_equipments", "local_services", "unlocalised_equipments",
    "quays", "access_spaces", "path_links", "path_junctions", "accesses", "navigation_paths", "rail_submode",
)


def urn_segment(value):
    return urllib.parse.quote(value, safe="-._~!$&'()*+,;=@")

def station_urn_plc(plc):
    return "urn:bt4pt:station:plc:" + urn_segment(plc)

def company_urn_org_code(org_code):
    return "urn:bt4pt:company:org:" + urn_segment(org_code.upper())


@dataclasses.dataclass
class Location:
    country: str
    plc: str
    name: str
    infrastructure_manager: str
    created: datetime.datetime
    last_modified: datetime.datetime
    name_ascii: typing.Optional[str] = None
    position: typing.Optional[typing.Tuple[decimal.Decimal, decimal.Decimal]] = None
    free_text: typing.Optional[str] = None


@dataclasses.dataclass
class Company:
    org_code: str
    country: str
    name: str
    short_name: str
    is_passenger: bool
    is_freight: bool
    is_infrastructure: bool
    is_other_company: bool
    is_national_entity: bool
    is_central_entity: bool
    is_current: bool
    created: datetime.datetime
    last_modified: datetime.datetime
    name_ascii: typing.Optional[str] = None
    url: typing.Optional[str] = None
    contact_person: typing.Optional[str] = None
    email: typing.Optional[str] = None
    phone: typing.Optional[str] = None
    mobile: typing.Optional[str] = None
    fax: typing.Optional[str] = None
    address: typing.Optional[str] = None
    city: typing.Optional[str] = None
    postal_code: typing.Optional[str] = None


def load_era_companies(path: pathlib.Path):
    parser = xsdata.formats.dataclass.parsers.XmlParser(
        config=xsdata.formats.dataclass.parsers.config.ParserConfig(
            fail_on_unknown_properties=True
        )
    )
    companies = parser.parse(path, models.crd.Companies).company
    today = datetime.date.today()
    for company in companies:
        start_validity = datetime.date.fromisoformat(company.start_validity.value)
        end_validity = datetime.date.fromisoformat(company.end_validity.value) if company.end_validity else None
        is_current = company.active_flag.value and start_validity <= today \
            and (end_validity is None or end_validity >= today)

        created = datetime.date.fromisoformat(company.add_date.value)
        last_modified = datetime.date.fromisoformat(company.modified_date.value) if company.modified_date else created

        yield Company(
            org_code=company.company_uic_code.value,
            country=company.country_iso_code.value,
            name=company.company_name.value,
            short_name=company.company_short_name.value,
            is_passenger=company.passenger_ru_flag.value,
            is_freight=company.freight_ru_flag.value,
            is_infrastructure=company.infrastructure_flag.value,
            is_other_company=company.other_company_flag.value,
            is_national_entity=company.national_entity_flag.value,
            is_central_entity=company.central_entity_flag.value,
            is_current=is_current,
            created=datetime.datetime.combine(created, datetime.time.min, tzinfo=datetime.UTC),
            last_modified=datetime.datetime.combine(last_modified, datetime.time.min, tzinfo=datetime.UTC),
            name_ascii=company.company_name_ascii.value
                if company.company_name_ascii and company.company_name_ascii.value != company.company_name.value
                else None,
            url=company.company_url.value or None if company.company_url else None,
            contact_person=company.contact_details.contact_person.value \
                if company.contact_details.contact_person.value.lower() != "unknown" else None,
            email=company.contact_details.email.value or None if company.contact_details.email else None,
            phone=company.contact_details.phone_number.value or None if company.contact_details.phone_number else None,
            fax=company.contact_details.fax_number.value or None if company.contact_details.fax_number else None,
            mobile=company.contact_details.mobile_number.value or None if company.contact_details.mobile_number else None,
            address=company.contact_details.address.value or None if company.contact_details.address else None,
            city=company.contact_details.city.value or None if company.contact_details.city else None,
            postal_code=company.contact_details.postal_code.value or None if company.contact_details.postal_code else None,
        )


def load_era_primary_locations(path: pathlib.Path):
    parser = xsdata.formats.dataclass.parsers.XmlParser(
        config=xsdata.formats.dataclass.parsers.config.ParserConfig(
            fail_on_unknown_properties=True
        )
    )
    locations = parser.parse(path, models.crd.PrimaryLocations).primary_location
    today = datetime.date.today()
    for location in locations:
        if not location.active_flag.value:
            continue
        if not location.passenger_possible_flag or not location.passenger_possible_flag.value:
            continue

        location_code = int(location.location_code.value)
        start_validity = datetime.date.fromisoformat(location.start_validity.value)
        end_validity = datetime.date.fromisoformat(location.end_validity.value) if location.end_validity else None
        passenger_start_validity = datetime.date.fromisoformat(location.passenger_start_validity.value) if location.passenger_start_validity else None
        passenger_end_validity = datetime.date.fromisoformat(location.passenger_end_validity.value) if location.passenger_end_validity else None
        if start_validity > today:
            continue
        if end_validity and end_validity < today:
            continue
        if passenger_start_validity and passenger_start_validity > today:
            continue
        if passenger_end_validity and passenger_end_validity < today:
            continue

        if location.latitude and location.latitude.value and location.longitude and location.longitude.value:
            position = (location.latitude.value, location.longitude.value)
        else:
            position = None

        created = datetime.date.fromisoformat(location.add_date.value)
        last_modified = datetime.date.fromisoformat(location.modified_date.value) if location.modified_date else created

        yield Location(
            country=location.country_iso_code.value,
            plc=f"{location.country_iso_code.value}{location_code}",
            name=location.location_name.value,
            name_ascii=location.location_name_ascii.value
                if location.location_name_ascii and location.location_name_ascii.value != location.location_name.value
                else None,
            position=position,
            infrastructure_manager=location.responsible_im.value,
            created=datetime.datetime.combine(created, datetime.time.min, tzinfo=datetime.UTC),
            last_modified=datetime.datetime.combine(last_modified, datetime.time.min, tzinfo=datetime.UTC),
            free_text=(location.free_text.value or None) if location.free_text else None,
        )

@dataclasses.dataclass
class DbNetex:
    stop_places: typing.List[models.netex.StopPlace]
    types_of_value: typing.Optional[models.netex.TypesOfValueInFrameRelStructure]
    codespaces: typing.List[models.netex.Codespace]


def load_db_netex() -> DbNetex:
    with requests.get(DB_NETEX_URL, stream=True) as r:
        r.raise_for_status()
        r.raw.decode_content = True
        parser = xsdata.formats.dataclass.parsers.XmlParser(
            config=xsdata.formats.dataclass.parsers.config.ParserConfig(
                fail_on_unknown_properties=True
            )
        )
        db_netex = parser.parse(r.raw, models.netex.PublicationDelivery)

    stop_places, types_of_value, codespaces = None, None, []
    for comp_frame in db_netex.data_objects.composite_frame:
        if comp_frame.codespaces:
            codespaces.extend(comp_frame.codespaces.codespace)
        for site_frame in comp_frame.frames.site_frame:
            if site_frame.type_of_frame_ref and site_frame.type_of_frame_ref.ref == "epip:EU_PI_STOP":
                stop_places = site_frame.stop_places.stop_place
        for resource_frame in comp_frame.frames.resource_frame:
            if resource_frame.types_of_value:
                types_of_value = resource_frame.types_of_value

    if stop_places is None:
        raise RuntimeError("Cannot find STOP PLACE site frame in DB data")
    return DbNetex(stop_places=stop_places, types_of_value=types_of_value, codespaces=codespaces)

def match_db_stop_places(
        locations: typing.Iterable[Location],
        stop_places: typing.Iterable[models.netex.StopPlace]
) -> typing.Dict[str, models.netex.StopPlace]:
    db_by_ril = {}
    for stop_place in stop_places:
        if not stop_place.key_list:
            continue
        ril_codes = [kv.value.strip() for kv in stop_place.key_list.key_value if kv.key == "RIL"]
        for rank, ril_code in enumerate(ril_codes):
            db_by_ril[ril_code] = (stop_place, rank)

    best = {}
    for location in locations:
        if location.infrastructure_manager not in DB_INFRASTRUCTURE_MANAGERS or not location.free_text:
            continue
        match = db_by_ril.get(location.free_text.strip())
        if match is None:
            continue
        db_stop_place, rank = match
        if db_stop_place.id not in best or rank < best[db_stop_place.id][0]:
            best[db_stop_place.id] = (rank, location.plc, db_stop_place)
    return {plc: db_stop_place for _, plc, db_stop_place in best.values()}


def make_netex_delivery(
        companies: typing.Iterable[Company],
        locations: typing.Iterable[Location],
        db: DbNetex,
        out
):
    locations = list(locations)
    db_by_plc = match_db_stop_places(locations, db.stop_places)
    db_codespace_urls = {codespace.id: codespace.xmlns_url for codespace in db.codespaces}

    operator = []
    for company in companies:
        org_types = []
        if company.is_passenger:
            org_types.append(models.netex.OrganisationTypeEnumeration.OPERATOR)
        if company.is_freight:
            org_types.append(models.netex.OrganisationTypeEnumeration.RAIL_FREIGHT_OPERATOR)
        if company.is_other_company:
            org_types.append(models.netex.OrganisationTypeEnumeration.OTHER)
        if company.is_infrastructure:
            org_types.append(models.netex.OrganisationTypeEnumeration.FACILITY_OPERATOR)
        if company.is_central_entity:
            org_types.append(models.netex.OrganisationTypeEnumeration.AUTHORITY)
        if company.is_national_entity:
            org_types.append(models.netex.OrganisationTypeEnumeration.STATUTORY_BODY)

        operator.append(models.netex.Operator(
            id=company_urn_org_code(company.org_code),
            created=company.created.isoformat(),
            changed=company.last_modified.isoformat(),
            version=int(company.last_modified.timestamp()),
            status_attribute=models.netex.StatusEnumeration.ACTIVE if company.is_current
                else models.netex.StatusEnumeration.INACTIVE,
            country_ref=company.country,
            name=models.netex.MultilingualString(
                content=[models.netex.TextType(
                    value=company.name
                )]
            ),
            short_name=models.netex.MultilingualString(
                content=[models.netex.TextType(
                    value=company.short_name
                )]
            ),
            alternative_names=models.netex.AlternativeNamesRelStructure(
                alternative_name=[models.netex.AlternativeName(
                    name_type=models.netex.NameTypeEnumeration.ALIAS,
                    name=models.netex.MultilingualString(
                        content=[models.netex.TextType(
                            value=company.name_ascii
                        )]
                    ),
                )]
            ) if company.name_ascii else None,
            organisation_type=org_types,
            contact_details=models.netex.ContactStructure(
                contact_person=models.netex.MultilingualString(
                    content=[models.netex.TextType(
                        value=company.contact_person
                    )]
                ) if company.contact_person else None,
                email=company.email,
                phone=company.phone,
                fax=company.fax,
                url=company.url,
            ),
            address=models.netex.TransportOrganisationVersionStructure.Address(
                address_line1=company.address,
                town=company.city,
                post_code=company.postal_code
            )
        ))

    stop_place = []
    for location in locations:
        netex_loc = models.netex.StopPlace(
            id=station_urn_plc(location.plc),
            created=location.created.isoformat(),
            changed=location.last_modified.isoformat(),
            version=int(location.last_modified.timestamp()),
            name=models.netex.MultilingualString(
                content=[models.netex.TextType(
                    value=location.name
                )]
            ),
            alternative_names=models.netex.AlternativeNamesRelStructure(
                alternative_name=[models.netex.AlternativeName(
                    name_type=models.netex.NameTypeEnumeration.ALIAS,
                    name=models.netex.MultilingualString(
                        content=[models.netex.TextType(
                            value=location.name_ascii
                        )]
                    ),
                )]
            ) if location.name_ascii else None,
            operator_ref=models.netex.OperatorRef(
                ref=company_urn_org_code(location.infrastructure_manager)
            ),
            transport_mode=models.netex.AllPublicTransportModesEnumeration.RAIL,
            stop_place_type=models.netex.StopTypeEnumeration.RAIL_STATION,
            centroid=models.netex.SimplePointVersionStructure(
                location=models.netex.LocationStructure2(
                    latitude=location.position[0],
                    longitude=location.position[1],
                )
            ) if location.position else None,
        )
        if location.plc in db_by_plc:
            infill_im_data(netex_loc, db_by_plc[location.plc], db_codespace_urls)
        stop_place.append(netex_loc)

    codespaces = [models.netex.Codespace(
        id="epip",
        xmlns="epip",
        xmlns_url="http://netex-cen.eu/epip/",
    )]
    for codespace in db.codespaces:
        if codespace.id not in {c.id for c in codespaces}:
            codespaces.append(codespace)

    now = datetime.datetime.now(datetime.UTC).replace(microsecond=0)
    delivery = models.netex.PublicationDelivery(
        version="2.0",
        publication_timestamp=xsdata.models.datatype.XmlDateTime.from_datetime(now),
        participant_ref=models.netex.ParticipantRef(
            value=company_urn_org_code(DELIVERY_COMPANY_CODE)
        ),
        description=models.netex.MultilingualString(
            content=[models.netex.TextType(
                value="European Union Agency for Railways data, with additional data from Infrastructure Manager NeTEx feeds.",
                lang="en",
            )]
        ),
        data_objects=models.netex.DataObjectsRelStructure(
            resource_frame=[models.netex.ResourceFrame(
                id="https://as207960.net/netex/resource-frame",
                version=int(now.timestamp()),
                organisations=models.netex.OrganisationsInFrameRelStructure(
                    operator=operator,
                ),
                types_of_value=db.types_of_value,
            )],
            site_frame=[models.netex.SiteFrame(
                id="https://as207960.net/netex/site-frame",
                version=int(now.timestamp()),
                type_of_frame_ref=models.netex.TypeOfFrameRef(
                    ref="epip:EU_PI_STOP",
                    version_ref="1.0"
                ),
                codespaces=models.netex.CodespacesRelStructure(
                    codespace=codespaces,
                ),
                stop_places=models.netex.StopPlacesInFrameRelStructure(
                    stop_place=stop_place,
                )
            )]
        )
    )

    serializer = xsdata.formats.dataclass.serializers.XmlSerializer(
        config=xsdata.formats.dataclass.serializers.config.SerializerConfig(
            indent="  "
        )
    )
    serializer.write(out, delivery, {
        None: "http://www.netex.org.uk/netex"
    })


def infill_im_data(
        netex_loc: models.netex.StopPlace,
        im_stop_place: models.netex.StopPlace,
        codespace_urls: typing.Dict[str, str],
):
    for field in IM_COPIED_FIELDS:
        value = getattr(im_stop_place, field)
        if value is not None and value != []:
            setattr(netex_loc, field, value)
    if im_stop_place.parent_site_ref:
        if netex_loc.private_codes is None:
            netex_loc.private_codes = models.netex.PrivateCodes()
        netex_loc.private_codes.private_code.append(
            alternative_id_code(im_stop_place.parent_site_ref.ref, codespace_urls)
        )
    if im_stop_place.topographic_place_ref:
        netex_loc.additional_topographic_places = models.netex.TopographicPlaceRefsRelStructure(
            topographic_place_ref=[im_stop_place.topographic_place_ref]
        )
    retarget_refs([getattr(netex_loc, field) for field in IM_COPIED_FIELDS], im_stop_place.id, netex_loc.id)


def alternative_id_code(netex_id: str, codespace_urls: typing.Dict[str, str]) -> models.netex.PrivateCode:
    codespace, _, local_id = netex_id.partition(":")
    return models.netex.PrivateCode(
        value=local_id,
        type_value=codespace_urls.get(codespace, codespace),
    )


def retarget_refs(obj, old_ref: str, new_ref: str):
    if isinstance(obj, list):
        for item in obj:
            retarget_refs(item, old_ref, new_ref)
    elif dataclasses.is_dataclass(obj):
        for field in dataclasses.fields(obj):
            value = getattr(obj, field.name)
            if field.name == "ref" and value == old_ref:
                setattr(obj, field.name, new_ref)
            elif isinstance(value, list) or dataclasses.is_dataclass(value):
                retarget_refs(value, old_ref, new_ref)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--company", type=pathlib.Path, help="Company XML export from the RNE CRD", required=True)
    parser.add_argument("--plc", type=pathlib.Path, help="PrimaryLocations XML export from the RNE CRD", required=True)
    parser.add_argument("--output", type=pathlib.Path, help="Output file", required=True)
    args = parser.parse_args()

    db = load_db_netex()

    with open(args.output, "w", encoding="utf8") as f:
        make_netex_delivery(
            companies=load_era_companies(args.company),
            locations=load_era_primary_locations(args.plc),
            db=db,
            out=f
        )

if __name__ == "__main__":
    main()