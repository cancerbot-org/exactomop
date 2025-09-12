# Generated migration: create OMOP CDM core tables for Eunomia GiBleed (v5.3)
from django.db import migrations

SQL_UP = r"""
-- === OMOP CDM v5.3 Core Tables (subset covering Eunomia GiBleed) ===

CREATE TABLE IF NOT EXISTS public.cdm_source (
  cdm_source_name               varchar(255) NOT NULL,
  cdm_source_abbreviation       varchar(25) NULL,
  cdm_holder                    varchar(255) NULL,
  source_description            text NULL,
  source_documentation_reference varchar(255) NULL,
  cdm_etl_reference             varchar(255) NULL,
  source_release_date           date NULL,
  cdm_release_date              date NULL,
  cdm_version                   varchar(10) NULL,
  vocabulary_version            varchar(20) NULL
);

CREATE TABLE IF NOT EXISTS public.location (
  location_id                   bigint PRIMARY KEY,
  address_1                     varchar(50) NULL,
  address_2                     varchar(50) NULL,
  city                          varchar(50) NULL,
  state                         varchar(2) NULL,
  zip                           varchar(9) NULL,
  county                        varchar(20) NULL,
  location_source_value         varchar(50) NULL,
  country_concept_id            integer NULL
);

CREATE TABLE IF NOT EXISTS public.care_site (
  care_site_id                  bigint PRIMARY KEY,
  care_site_name                varchar(255) NULL,
  place_of_service_concept_id   integer NULL,
  location_id                   bigint NULL,
  care_site_source_value        varchar(50) NULL,
  place_of_service_source_value varchar(50) NULL
);

CREATE TABLE IF NOT EXISTS public.provider (
  provider_id                   bigint PRIMARY KEY,
  provider_name                 varchar(255) NULL,
  npi                           varchar(20) NULL,
  dea                           varchar(20) NULL,
  specialty_concept_id          integer NULL,
  care_site_id                  bigint NULL,
  year_of_birth                 integer NULL,
  gender_concept_id             integer NULL,
  provider_source_value         varchar(50) NULL,
  specialty_source_value        varchar(50) NULL,
  specialty_source_concept_id   integer NULL,
  gender_source_value           varchar(50) NULL,
  gender_source_concept_id      integer NULL
);

CREATE TABLE IF NOT EXISTS public.person (
  person_id                     bigint PRIMARY KEY,
  gender_concept_id             integer NOT NULL,
  year_of_birth                 integer NULL,
  month_of_birth                integer NULL,
  day_of_birth                  integer NULL,
  birth_datetime                timestamp NULL,
  race_concept_id               integer NULL,
  ethnicity_concept_id          integer NULL,
  location_id                   bigint NULL,
  provider_id                   bigint NULL,
  care_site_id                  bigint NULL,
  person_source_value           varchar(50) NULL,
  gender_source_value           varchar(50) NULL,
  gender_source_concept_id      integer NULL,
  race_source_value             varchar(50) NULL,
  race_source_concept_id        integer NULL,
  ethnicity_source_value        varchar(50) NULL,
  ethnicity_source_concept_id   integer NULL
);

CREATE TABLE IF NOT EXISTS public.observation_period (
  observation_period_id         bigint PRIMARY KEY,
  person_id                     bigint NOT NULL,
  observation_period_start_date date NOT NULL,
  observation_period_end_date   date NOT NULL,
  period_type_concept_id        integer NOT NULL
);

CREATE TABLE IF NOT EXISTS public.visit_occurrence (
  visit_occurrence_id           bigint PRIMARY KEY,
  person_id                     bigint NOT NULL,
  visit_concept_id              integer NOT NULL,
  visit_start_date              date NOT NULL,
  visit_start_datetime          timestamp NULL,
  visit_end_date                date NOT NULL,
  visit_end_datetime            timestamp NULL,
  visit_type_concept_id         integer NOT NULL,
  provider_id                   bigint NULL,
  care_site_id                  bigint NULL,
  visit_source_value            varchar(50) NULL,
  visit_source_concept_id       integer NULL,
  admitting_source_concept_id   integer NULL,
  discharge_to_concept_id       integer NULL,
  preceding_visit_occurrence_id bigint NULL
);

CREATE TABLE IF NOT EXISTS public.condition_occurrence (
  condition_occurrence_id       bigint PRIMARY KEY,
  person_id                     bigint NOT NULL,
  condition_concept_id          integer NOT NULL,
  condition_start_date          date NOT NULL,
  condition_start_datetime      timestamp NULL,
  condition_end_date            date NULL,
  condition_end_datetime        timestamp NULL,
  condition_type_concept_id     integer NOT NULL,
  stop_reason                   varchar(20) NULL,
  provider_id                   bigint NULL,
  visit_occurrence_id           bigint NULL,
  visit_detail_id               bigint NULL,
  condition_source_value        varchar(50) NULL,
  condition_source_concept_id   integer NULL,
  condition_status_source_value varchar(50) NULL,
  condition_status_concept_id   integer NULL
);

CREATE TABLE IF NOT EXISTS public.drug_exposure (
  drug_exposure_id              bigint PRIMARY KEY,
  person_id                     bigint NOT NULL,
  drug_concept_id               integer NOT NULL,
  drug_exposure_start_date      date NOT NULL,
  drug_exposure_start_datetime  timestamp NULL,
  drug_exposure_end_date        date NULL,
  drug_exposure_end_datetime    timestamp NULL,
  verbatim_end_date             date NULL,
  drug_type_concept_id          integer NOT NULL,
  stop_reason                   varchar(20) NULL,
  refills                       integer NULL,
  quantity                      numeric NULL,
  days_supply                   integer NULL,
  sig                           text NULL,
  route_concept_id              integer NULL,
  lot_number                    varchar(50) NULL,
  provider_id                   bigint NULL,
  visit_occurrence_id           bigint NULL,
  visit_detail_id               bigint NULL,
  drug_source_value             varchar(50) NULL,
  drug_source_concept_id        integer NULL,
  route_source_value            varchar(50) NULL,
  dose_unit_source_value        varchar(50) NULL
);

CREATE TABLE IF NOT EXISTS public.procedure_occurrence (
  procedure_occurrence_id       bigint PRIMARY KEY,
  person_id                     bigint NOT NULL,
  procedure_concept_id          integer NOT NULL,
  procedure_date                date NOT NULL,
  procedure_datetime            timestamp NULL,
  procedure_type_concept_id     integer NOT NULL,
  modifier_concept_id           integer NULL,
  quantity                      integer NULL,
  provider_id                   bigint NULL,
  visit_occurrence_id           bigint NULL,
  visit_detail_id               bigint NULL,
  procedure_source_value        varchar(50) NULL,
  procedure_source_concept_id   integer NULL,
  modifier_source_value         varchar(50) NULL
);

CREATE TABLE IF NOT EXISTS public.device_exposure (
  device_exposure_id            bigint PRIMARY KEY,
  person_id                     bigint NOT NULL,
  device_concept_id             integer NOT NULL,
  device_exposure_start_date    date NOT NULL,
  device_exposure_start_datetime timestamp NULL,
  device_exposure_end_date      date NULL,
  device_exposure_end_datetime  timestamp NULL,
  device_type_concept_id        integer NOT NULL,
  unique_device_id              varchar(255) NULL,
  quantity                      integer NULL,
  provider_id                   bigint NULL,
  visit_occurrence_id           bigint NULL,
  visit_detail_id               bigint NULL,
  device_source_value           varchar(100) NULL,
  device_source_concept_id      integer NULL
);

CREATE TABLE IF NOT EXISTS public.measurement (
  measurement_id                bigint PRIMARY KEY,
  person_id                     bigint NOT NULL,
  measurement_concept_id        integer NOT NULL,
  measurement_date              date NOT NULL,
  measurement_datetime          timestamp NULL,
  measurement_time              varchar(10) NULL,
  measurement_type_concept_id   integer NOT NULL,
  operator_concept_id           integer NULL,
  value_as_number               numeric NULL,
  value_as_concept_id           integer NULL,
  unit_concept_id               integer NULL,
  range_low                     numeric NULL,
  range_high                    numeric NULL,
  provider_id                   bigint NULL,
  visit_occurrence_id           bigint NULL,
  visit_detail_id               bigint NULL,
  measurement_source_value      varchar(50) NULL,
  measurement_source_concept_id integer NULL,
  unit_source_value             varchar(50) NULL,
  value_source_value            varchar(50) NULL
);

CREATE TABLE IF NOT EXISTS public.observation (
  observation_id                bigint PRIMARY KEY,
  person_id                     bigint NOT NULL,
  observation_concept_id        integer NOT NULL,
  observation_date              date NOT NULL,
  observation_datetime          timestamp NULL,
  observation_type_concept_id   integer NOT NULL,
  value_as_number               numeric NULL,
  value_as_string               varchar(60) NULL,
  value_as_concept_id           integer NULL,
  qualifier_concept_id          integer NULL,
  unit_concept_id               integer NULL,
  provider_id                   bigint NULL,
  visit_occurrence_id           bigint NULL,
  visit_detail_id               bigint NULL,
  observation_source_value      varchar(50) NULL,
  observation_source_concept_id integer NULL,
  unit_source_value             varchar(50) NULL,
  qualifier_source_value        varchar(50) NULL
);

CREATE TABLE IF NOT EXISTS public.death (
  person_id                     bigint PRIMARY KEY,
  death_date                    date NOT NULL,
  death_datetime                timestamp NULL,
  death_type_concept_id         integer NULL,
  cause_concept_id              integer NULL,
  cause_source_value            varchar(50) NULL,
  cause_source_concept_id       integer NULL
);

CREATE TABLE IF NOT EXISTS public.payer_plan_period (
  payer_plan_period_id          bigint PRIMARY KEY,
  person_id                     bigint NOT NULL,
  payer_plan_period_start_date  date NOT NULL,
  payer_plan_period_end_date    date NOT NULL,
  payer_concept_id              integer NULL,
  payer_source_value            varchar(50) NULL,
  payer_source_concept_id       integer NULL,
  plan_concept_id               integer NULL,
  plan_source_value             varchar(50) NULL,
  plan_source_concept_id        integer NULL,
  sponsor_concept_id            integer NULL,
  sponsor_source_value          varchar(50) NULL,
  sponsor_source_concept_id     integer NULL,
  family_source_value           varchar(50) NULL,
  stop_reason_concept_id        integer NULL,
  stop_reason_source_value      varchar(50) NULL,
  stop_reason_source_concept_id integer NULL
);

CREATE TABLE IF NOT EXISTS public.cost (
  cost_id                       bigint PRIMARY KEY,
  cost_event_id                 bigint NOT NULL,
  cost_domain_id                varchar(20) NOT NULL,
  cost_type_concept_id          integer NOT NULL,
  currency_concept_id           integer NULL,
  total_charge                  numeric NULL,
  total_cost                    numeric NULL,
  total_paid                    numeric NULL,
  paid_by_payer                 numeric NULL,
  paid_by_patient               numeric NULL,
  paid_patient_copay            numeric NULL,
  paid_patient_coinsurance      numeric NULL,
  paid_patient_deductible       numeric NULL,
  paid_by_primary               numeric NULL,
  paid_ingredient_cost          numeric NULL,
  paid_dispensing_fee           numeric NULL,
  payer_plan_period_id          bigint NULL,
  amount_allowed                numeric NULL,
  revenue_code_concept_id       integer NULL,
  drg_concept_id                integer NULL,
  revenue_code_source_value     varchar(50) NULL,
  drg_source_value              varchar(3) NULL
);
"""
SQL_DOWN = r"""
-- drop core tables (order matters due to FKs if you add them later)
DROP TABLE IF EXISTS public.cost;
DROP TABLE IF EXISTS public.payer_plan_period;
DROP TABLE IF EXISTS public.death;
DROP TABLE IF EXISTS public.observation;
DROP TABLE IF EXISTS public.measurement;
DROP TABLE IF EXISTS public.device_exposure;
DROP TABLE IF EXISTS public.procedure_occurrence;
DROP TABLE IF EXISTS public.drug_exposure;
DROP TABLE IF EXISTS public.condition_occurrence;
DROP TABLE IF EXISTS public.visit_occurrence;
DROP TABLE IF EXISTS public.observation_period;
DROP TABLE IF EXISTS public.person;
DROP TABLE IF EXISTS public.provider;
DROP TABLE IF EXISTS public.care_site;
DROP TABLE IF EXISTS public.location;
DROP TABLE IF EXISTS public.cdm_source;
"""

class Migration(migrations.Migration):
    dependencies = [
        ('omop', '0001_initial'),  # adjust if your initial migration has a different name
    ]

    operations = [
        migrations.RunSQL(SQL_UP, reverse_sql=SQL_DOWN),
    ]
