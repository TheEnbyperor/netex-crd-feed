from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "http://ws.refdata.crd.cc.uic.org/replication/schemas"


@dataclass(kw_only=True)
class ActiveFlag:
    class Meta:
        name = "Active_Flag"
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: bool = field()


@dataclass(kw_only=True)
class AddDate:
    class Meta:
        name = "Add_Date"
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: str = field(
        default="",
        metadata={
            "pattern": r"\d{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])",
        },
    )


@dataclass(kw_only=True)
class Address:
    class Meta:
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: str = field(
        default="",
        metadata={
            "min_length": 1,
            "max_length": 255,
        },
    )


@dataclass(kw_only=True)
class AllocationCompany:
    class Meta:
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: str = field(
        default="",
        metadata={
            "min_length": 4,
            "max_length": 4,
        },
    )


@dataclass(kw_only=True)
class CentralEntityFlag:
    class Meta:
        name = "Central_Entity_Flag"
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: bool = field()


@dataclass(kw_only=True)
class City:
    class Meta:
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: str = field(
        default="",
        metadata={
            "min_length": 0,
            "max_length": 50,
        },
    )


@dataclass(kw_only=True)
class CompanyName:
    class Meta:
        name = "Company_Name"
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: str = field(
        default="",
        metadata={
            "min_length": 1,
            "max_length": 255,
        },
    )


@dataclass(kw_only=True)
class CompanyNameAscii:
    class Meta:
        name = "Company_Name_ASCII"
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: str = field(
        default="",
        metadata={
            "min_length": 1,
            "max_length": 255,
        },
    )


@dataclass(kw_only=True)
class CompanyShortName:
    class Meta:
        name = "Company_Short_Name"
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: str = field(
        default="",
        metadata={
            "min_length": 0,
            "max_length": 50,
        },
    )


@dataclass(kw_only=True)
class CompanyUicCode:
    class Meta:
        name = "Company_UIC_Code"
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: str = field(
        default="",
        metadata={
            "min_length": 4,
            "max_length": 4,
        },
    )


@dataclass(kw_only=True)
class CompanyUrl:
    class Meta:
        name = "Company_URL"
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: str = field(
        default="",
        metadata={
            "min_length": 0,
            "max_length": 100,
        },
    )


@dataclass(kw_only=True)
class ContactPerson:
    class Meta:
        name = "Contact_Person"
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: str = field(
        default="",
        metadata={
            "min_length": 1,
            "max_length": 255,
        },
    )


@dataclass(kw_only=True)
class ContainerHandlingFlag:
    class Meta:
        name = "Container_Handling_Flag"
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: bool = field()


@dataclass(kw_only=True)
class CountryIsoCode1:
    class Meta:
        name = "Country_ISO_Code"
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: str = field(
        default="",
        metadata={
            "min_length": 2,
            "max_length": 2,
        },
    )


@dataclass(kw_only=True)
class CountryIsoCode2:
    class Meta:
        name = "Country_Iso_Code"
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: str = field(
        default="",
        metadata={
            "min_length": 2,
            "max_length": 2,
        },
    )


@dataclass(kw_only=True)
class Email:
    class Meta:
        nillable = True
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: None | str = field(
        default="",
        metadata={
            "min_length": 0,
            "max_length": 70,
            "nillable": True,
        },
    )


@dataclass(kw_only=True)
class EndValidity:
    class Meta:
        name = "End_Validity"
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: str = field(
        default="",
        metadata={
            "pattern": r"\d{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])",
        },
    )


@dataclass(kw_only=True)
class FaxNumber:
    class Meta:
        name = "FAX_Number"
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: str = field(
        default="",
        metadata={
            "min_length": 0,
            "max_length": 70,
        },
    )


@dataclass(kw_only=True)
class FreeText:
    class Meta:
        name = "Free_Text"
        nillable = True
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: None | str = field(
        default="",
        metadata={
            "min_length": 0,
            "max_length": 255,
            "nillable": True,
        },
    )


@dataclass(kw_only=True)
class FreightEndValidity:
    class Meta:
        name = "Freight_End_Validity"
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: str = field(
        default="",
        metadata={
            "pattern": r"\d{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])",
        },
    )


@dataclass(kw_only=True)
class FreightPossibleFlag:
    class Meta:
        name = "Freight_Possible_Flag"
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: bool = field()


@dataclass(kw_only=True)
class FreightRuFlag:
    class Meta:
        name = "Freight_RU_Flag"
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: bool = field()


@dataclass(kw_only=True)
class FreightStartValidity:
    class Meta:
        name = "Freight_Start_Validity"
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: str = field(
        default="",
        metadata={
            "pattern": r"\d{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])",
        },
    )


@dataclass(kw_only=True)
class HandoverPointFlag:
    class Meta:
        name = "Handover_Point_Flag"
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: bool = field()


@dataclass(kw_only=True)
class InfrastructureFlag:
    class Meta:
        name = "Infrastructure_Flag"
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: bool = field()


@dataclass(kw_only=True)
class Latitude:
    class Meta:
        nillable = True
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: None | Decimal = field(
        metadata={
            "total_digits": 14,
            "fraction_digits": 6,
            "nillable": True,
        }
    )


@dataclass(kw_only=True)
class LocationCode:
    class Meta:
        name = "Location_Code"
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: str = field(
        default="",
        metadata={
            "min_length": 1,
            "max_length": 5,
        },
    )


@dataclass(kw_only=True)
class LocationName:
    class Meta:
        name = "Location_Name"
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: str = field(
        default="",
        metadata={
            "min_length": 0,
            "max_length": 255,
        },
    )


@dataclass(kw_only=True)
class LocationNameAscii:
    class Meta:
        name = "Location_Name_ASCII"
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: str = field(
        default="",
        metadata={
            "min_length": 0,
            "max_length": 255,
        },
    )


@dataclass(kw_only=True)
class Longitude:
    class Meta:
        nillable = True
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: None | Decimal = field(
        metadata={
            "total_digits": 15,
            "fraction_digits": 6,
            "nillable": True,
        }
    )


@dataclass(kw_only=True)
class MobileNumber:
    class Meta:
        name = "Mobile_Number"
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: str = field(
        default="",
        metadata={
            "min_length": 0,
            "max_length": 70,
        },
    )


@dataclass(kw_only=True)
class ModifiedDate:
    class Meta:
        name = "Modified_Date"
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: str = field(
        default="",
        metadata={
            "pattern": r"\d{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])",
        },
    )


@dataclass(kw_only=True)
class NutsCode:
    class Meta:
        name = "NUTS_Code"
        nillable = True
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: None | str = field(
        default="",
        metadata={
            "max_length": 5,
            "nillable": True,
        },
    )


@dataclass(kw_only=True)
class NationalEntityFlag:
    class Meta:
        name = "National_Entity_Flag"
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: bool = field()


@dataclass(kw_only=True)
class OtherCompanyFlag:
    class Meta:
        name = "Other_Company_flag"
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: bool = field()


@dataclass(kw_only=True)
class PassengerEndValidity:
    class Meta:
        name = "Passenger_End_Validity"
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: str = field(
        default="",
        metadata={
            "pattern": r"\d{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])",
        },
    )


@dataclass(kw_only=True)
class PassengerPossibleFlag:
    class Meta:
        name = "Passenger_Possible_Flag"
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: bool = field()


@dataclass(kw_only=True)
class PassengerRuFlag:
    class Meta:
        name = "Passenger_RU_Flag"
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: bool = field()


@dataclass(kw_only=True)
class PassengerStartValidity:
    class Meta:
        name = "Passenger_Start_Validity"
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: str = field(
        default="",
        metadata={
            "pattern": r"\d{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])",
        },
    )


@dataclass(kw_only=True)
class PhoneNumber:
    class Meta:
        name = "Phone_Number"
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: str = field(
        default="",
        metadata={
            "min_length": 0,
            "max_length": 70,
        },
    )


@dataclass(kw_only=True)
class PostalCode:
    class Meta:
        name = "Postal_Code"
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: str = field(
        default="",
        metadata={
            "max_length": 10,
        },
    )


@dataclass(kw_only=True)
class ResponsibleIm:
    class Meta:
        name = "ResponsibleIM"
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: str = field(
        default="",
        metadata={
            "min_length": 4,
            "max_length": 4,
        },
    )


@dataclass(kw_only=True)
class ResponsibleImCode:
    class Meta:
        name = "Responsible_IM_Code"
        nillable = True
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: None | str = field(
        default="",
        metadata={
            "min_length": 4,
            "max_length": 4,
            "nillable": True,
        },
    )


@dataclass(kw_only=True)
class StartValidity:
    class Meta:
        name = "Start_Validity"
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: str = field(
        default="",
        metadata={
            "pattern": r"\d{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])",
        },
    )


@dataclass(kw_only=True)
class SubsidiaryLocationCode:
    class Meta:
        name = "Subsidiary_Location_Code"
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: str = field(
        default="",
        metadata={
            "min_length": 1,
            "max_length": 10,
        },
    )


@dataclass(kw_only=True)
class SubsidiaryLocationName:
    class Meta:
        name = "Subsidiary_Location_Name"
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: str = field(
        default="",
        metadata={
            "min_length": 0,
            "max_length": 255,
        },
    )


@dataclass(kw_only=True)
class SubsidiaryTypeCode:
    class Meta:
        name = "Subsidiary_Type_Code"
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    value: str = field(
        default="",
        metadata={
            "max_length": 2,
        },
    )


@dataclass(kw_only=True)
class Companies:
    class Meta:
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    company: list[Companies.Company] = field(
        default_factory=list,
        metadata={
            "name": "Company",
            "type": "Element",
        },
    )

    @dataclass(kw_only=True)
    class Company:
        company_name: CompanyName = field(
            metadata={
                "name": "Company_Name",
                "type": "Element",
            }
        )
        company_name_ascii: None | CompanyNameAscii = field(
            default=None,
            metadata={
                "name": "Company_Name_ASCII",
                "type": "Element",
            },
        )
        company_uic_code: CompanyUicCode = field(
            metadata={
                "name": "Company_UIC_Code",
                "type": "Element",
            }
        )
        company_url: None | CompanyUrl = field(
            default=None,
            metadata={
                "name": "Company_URL",
                "type": "Element",
            },
        )
        country_iso_code: CountryIsoCode1 = field(
            metadata={
                "name": "Country_ISO_Code",
                "type": "Element",
            }
        )
        start_validity: StartValidity = field(
            metadata={
                "name": "Start_Validity",
                "type": "Element",
            }
        )
        end_validity: None | EndValidity = field(
            default=None,
            metadata={
                "name": "End_Validity",
                "type": "Element",
            },
        )
        company_short_name: CompanyShortName = field(
            metadata={
                "name": "Company_Short_Name",
                "type": "Element",
            }
        )
        free_text: None | FreeText = field(
            default=None,
            metadata={
                "name": "Free_Text",
                "type": "Element",
                "nillable": True,
            },
        )
        contact_details: Companies.Company.ContactDetails = field(
            metadata={
                "name": "Contact_Details",
                "type": "Element",
            }
        )
        passenger_ru_flag: PassengerRuFlag = field(
            metadata={
                "name": "Passenger_RU_Flag",
                "type": "Element",
            }
        )
        freight_ru_flag: FreightRuFlag = field(
            metadata={
                "name": "Freight_RU_Flag",
                "type": "Element",
            }
        )
        infrastructure_flag: InfrastructureFlag = field(
            metadata={
                "name": "Infrastructure_Flag",
                "type": "Element",
            }
        )
        other_company_flag: OtherCompanyFlag = field(
            metadata={
                "name": "Other_Company_flag",
                "type": "Element",
            }
        )
        national_entity_flag: NationalEntityFlag = field(
            metadata={
                "name": "National_Entity_Flag",
                "type": "Element",
            }
        )
        central_entity_flag: CentralEntityFlag = field(
            metadata={
                "name": "Central_Entity_Flag",
                "type": "Element",
            }
        )
        active_flag: ActiveFlag = field(
            metadata={
                "name": "Active_Flag",
                "type": "Element",
            }
        )
        add_date: AddDate = field(
            metadata={
                "name": "Add_Date",
                "type": "Element",
            }
        )
        modified_date: None | ModifiedDate = field(
            default=None,
            metadata={
                "name": "Modified_Date",
                "type": "Element",
            },
        )

        @dataclass(kw_only=True)
        class ContactDetails:
            contact_person: ContactPerson = field(
                metadata={
                    "name": "Contact_Person",
                    "type": "Element",
                }
            )
            email: None | Email = field(
                default=None,
                metadata={
                    "name": "Email",
                    "type": "Element",
                    "nillable": True,
                },
            )
            phone_number: None | PhoneNumber = field(
                default=None,
                metadata={
                    "name": "Phone_Number",
                    "type": "Element",
                },
            )
            fax_number: None | FaxNumber = field(
                default=None,
                metadata={
                    "name": "FAX_Number",
                    "type": "Element",
                },
            )
            address: None | Address = field(
                default=None,
                metadata={
                    "name": "Address",
                    "type": "Element",
                },
            )
            city: None | City = field(
                default=None,
                metadata={
                    "name": "City",
                    "type": "Element",
                },
            )
            mobile_number: None | MobileNumber = field(
                default=None,
                metadata={
                    "name": "Mobile_Number",
                    "type": "Element",
                },
            )
            postal_code: None | PostalCode = field(
                default=None,
                metadata={
                    "name": "Postal_Code",
                    "type": "Element",
                },
            )


@dataclass(kw_only=True)
class PrimaryLocations:
    class Meta:
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    primary_location: list[PrimaryLocations.PrimaryLocation] = field(
        default_factory=list,
        metadata={
            "name": "Primary_Location",
            "type": "Element",
        },
    )

    @dataclass(kw_only=True)
    class PrimaryLocation:
        country_iso_code: CountryIsoCode2 = field(
            metadata={
                "name": "Country_Iso_Code",
                "type": "Element",
            }
        )
        location_code: LocationCode = field(
            metadata={
                "name": "Location_Code",
                "type": "Element",
            }
        )
        start_validity: StartValidity = field(
            metadata={
                "name": "Start_Validity",
                "type": "Element",
            }
        )
        end_validity: None | EndValidity = field(
            default=None,
            metadata={
                "name": "End_Validity",
                "type": "Element",
            },
        )
        responsible_im: ResponsibleIm = field(
            metadata={
                "name": "ResponsibleIM",
                "type": "Element",
            }
        )
        location_name: LocationName = field(
            metadata={
                "name": "Location_Name",
                "type": "Element",
            }
        )
        location_name_ascii: LocationNameAscii = field(
            metadata={
                "name": "Location_Name_ASCII",
                "type": "Element",
            }
        )
        nuts_code: None | NutsCode = field(
            default=None,
            metadata={
                "name": "NUTS_Code",
                "type": "Element",
                "nillable": True,
            },
        )
        container_handling_flag: None | ContainerHandlingFlag = field(
            default=None,
            metadata={
                "name": "Container_Handling_Flag",
                "type": "Element",
            },
        )
        handover_point_flag: None | HandoverPointFlag = field(
            default=None,
            metadata={
                "name": "Handover_Point_Flag",
                "type": "Element",
            },
        )
        freight_possible_flag: None | FreightPossibleFlag = field(
            default=None,
            metadata={
                "name": "Freight_Possible_Flag",
                "type": "Element",
            },
        )
        freight_start_validity: None | FreightStartValidity = field(
            default=None,
            metadata={
                "name": "Freight_Start_Validity",
                "type": "Element",
            },
        )
        freight_end_validity: None | FreightEndValidity = field(
            default=None,
            metadata={
                "name": "Freight_End_Validity",
                "type": "Element",
            },
        )
        passenger_possible_flag: None | PassengerPossibleFlag = field(
            default=None,
            metadata={
                "name": "Passenger_Possible_Flag",
                "type": "Element",
            },
        )
        passenger_start_validity: None | PassengerStartValidity = field(
            default=None,
            metadata={
                "name": "Passenger_Start_Validity",
                "type": "Element",
            },
        )
        passenger_end_validity: None | PassengerEndValidity = field(
            default=None,
            metadata={
                "name": "Passenger_End_Validity",
                "type": "Element",
            },
        )
        free_text: None | FreeText = field(
            default=None,
            metadata={
                "name": "Free_Text",
                "type": "Element",
                "nillable": True,
            },
        )
        latitude: None | Latitude = field(
            default=None,
            metadata={
                "name": "Latitude",
                "type": "Element",
                "nillable": True,
            },
        )
        longitude: None | Longitude = field(
            default=None,
            metadata={
                "name": "Longitude",
                "type": "Element",
                "nillable": True,
            },
        )
        active_flag: ActiveFlag = field(
            metadata={
                "name": "Active_Flag",
                "type": "Element",
            }
        )
        add_date: AddDate = field(
            metadata={
                "name": "Add_Date",
                "type": "Element",
            }
        )
        modified_date: None | ModifiedDate = field(
            default=None,
            metadata={
                "name": "Modified_Date",
                "type": "Element",
            },
        )


@dataclass(kw_only=True)
class SubsidiaryLocations:
    """
    :ivar subsidiary_location: Subsidiary Type information
    """

    class Meta:
        namespace = "http://ws.refdata.crd.cc.uic.org/replication/schemas"

    subsidiary_location: list[SubsidiaryLocations.SubsidiaryLocation] = field(
        default_factory=list,
        metadata={
            "name": "Subsidiary_Location",
            "type": "Element",
        },
    )

    @dataclass(kw_only=True)
    class SubsidiaryLocation:
        country_iso_code: None | CountryIsoCode2 = field(
            default=None,
            metadata={
                "name": "Country_Iso_Code",
                "type": "Element",
            },
        )
        responsible_im_code: None | ResponsibleImCode = field(
            default=None,
            metadata={
                "name": "Responsible_IM_Code",
                "type": "Element",
                "nillable": True,
            },
        )
        subsidiary_location_code: SubsidiaryLocationCode = field(
            metadata={
                "name": "Subsidiary_Location_Code",
                "type": "Element",
            }
        )
        location_code: LocationCode = field(
            metadata={
                "name": "Location_Code",
                "type": "Element",
            }
        )
        subsidiary_type_code: SubsidiaryTypeCode = field(
            metadata={
                "name": "Subsidiary_Type_Code",
                "type": "Element",
            }
        )
        subsidiary_location_name: SubsidiaryLocationName = field(
            metadata={
                "name": "Subsidiary_Location_Name",
                "type": "Element",
            }
        )
        start_validity: StartValidity = field(
            metadata={
                "name": "Start_Validity",
                "type": "Element",
            }
        )
        end_validity: None | EndValidity = field(
            default=None,
            metadata={
                "name": "End_Validity",
                "type": "Element",
            },
        )
        allocation_company: AllocationCompany = field(
            metadata={
                "name": "AllocationCompany",
                "type": "Element",
            }
        )
        latitude: None | Latitude = field(
            default=None,
            metadata={
                "name": "Latitude",
                "type": "Element",
                "nillable": True,
            },
        )
        longitude: None | Longitude = field(
            default=None,
            metadata={
                "name": "Longitude",
                "type": "Element",
                "nillable": True,
            },
        )
        free_text: None | FreeText = field(
            default=None,
            metadata={
                "name": "Free_Text",
                "type": "Element",
                "nillable": True,
            },
        )
        active_flag: ActiveFlag = field(
            metadata={
                "name": "Active_Flag",
                "type": "Element",
            }
        )
        add_date: AddDate = field(
            metadata={
                "name": "Add_Date",
                "type": "Element",
            }
        )
        modified_date: None | ModifiedDate = field(
            default=None,
            metadata={
                "name": "Modified_Date",
                "type": "Element",
            },
        )
