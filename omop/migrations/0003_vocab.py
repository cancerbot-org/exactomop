# Generated migration: create OMOP vocabulary tables for Eunomia GiBleed (v5.3)
from django.db import migrations

SQL_UP = r"""
-- === OMOP Vocabulary Tables (subset) ===
CREATE TABLE IF NOT EXISTS public.vocabulary (
  vocabulary_id                 varchar(20) PRIMARY KEY,
  vocabulary_name               varchar(255) NOT NULL,
  vocabulary_reference          varchar(255) NULL,
  vocabulary_version            varchar(255) NULL,
  vocabulary_concept_id         integer NOT NULL
);

CREATE TABLE IF NOT EXISTS public.domain (
  domain_id                     varchar(20) PRIMARY KEY,
  domain_name                   varchar(255) NOT NULL,
  domain_concept_id             integer NOT NULL
);

CREATE TABLE IF NOT EXISTS public.concept_class (
  concept_class_id              varchar(20) PRIMARY KEY,
  concept_class_name            varchar(255) NOT NULL,
  concept_class_concept_id      integer NOT NULL
);

CREATE TABLE IF NOT EXISTS public.relationship (
  relationship_id               varchar(20) PRIMARY KEY,
  relationship_name             varchar(255) NOT NULL,
  is_hierarchical               varchar(1) NOT NULL,
  defines_ancestry              varchar(1) NOT NULL,
  reverse_relationship_id       varchar(20) NOT NULL,
  relationship_concept_id       integer NOT NULL
);

CREATE TABLE IF NOT EXISTS public.concept (
  concept_id                    integer PRIMARY KEY,
  concept_name                  varchar(255) NOT NULL,
  domain_id                     varchar(20) NOT NULL,
  vocabulary_id                 varchar(20) NOT NULL,
  concept_class_id              varchar(20) NOT NULL,
  standard_concept              varchar(1) NULL,
  concept_code                  varchar(50) NOT NULL,
  valid_start_date              date NOT NULL,
  valid_end_date                date NOT NULL,
  invalid_reason                varchar(1) NULL
);

CREATE TABLE IF NOT EXISTS public.concept_relationship (
  concept_id_1                  integer NOT NULL,
  concept_id_2                  integer NOT NULL,
  relationship_id               varchar(20) NOT NULL,
  valid_start_date              date NOT NULL,
  valid_end_date                date NOT NULL,
  invalid_reason                varchar(1) NULL,
  PRIMARY KEY (concept_id_1, concept_id_2, relationship_id)
);

CREATE TABLE IF NOT EXISTS public.concept_ancestor (
  ancestor_concept_id           integer NOT NULL,
  descendant_concept_id         integer NOT NULL,
  min_levels_of_separation      integer NOT NULL,
  max_levels_of_separation      integer NOT NULL,
  PRIMARY KEY (ancestor_concept_id, descendant_concept_id)
);

CREATE TABLE IF NOT EXISTS public.concept_synonym (
  concept_id                    integer NOT NULL,
  concept_synonym_name          varchar(1000) NOT NULL,
  language_concept_id           integer NOT NULL
);

CREATE TABLE IF NOT EXISTS public.source_to_concept_map (
  source_code                   varchar(50) NOT NULL,
  source_concept_id             integer NOT NULL,
  source_vocabulary_id          varchar(20) NOT NULL,
  source_code_description       varchar(255) NULL,
  target_concept_id             integer NOT NULL,
  target_vocabulary_id          varchar(20) NOT NULL,
  valid_start_date              date NOT NULL,
  valid_end_date                date NOT NULL,
  invalid_reason                varchar(1) NULL
);

CREATE TABLE IF NOT EXISTS public.drug_strength (
  drug_concept_id               integer NOT NULL,
  ingredient_concept_id         integer NOT NULL,
  amount_value                  numeric NULL,
  amount_unit_concept_id        integer NULL,
  numerator_value               numeric NULL,
  numerator_unit_concept_id     integer NULL,
  denominator_value             numeric NULL,
  denominator_unit_concept_id   integer NULL,
  box_size                      integer NULL,
  valid_start_date              date NOT NULL,
  valid_end_date                date NOT NULL,
  invalid_reason                varchar(1) NULL,
  PRIMARY KEY (drug_concept_id, ingredient_concept_id)
);
"""
SQL_DOWN = r"""
DROP TABLE IF EXISTS public.drug_strength;
DROP TABLE IF EXISTS public.source_to_concept_map;
DROP TABLE IF EXISTS public.concept_synonym;
DROP TABLE IF EXISTS public.concept_ancestor;
DROP TABLE IF EXISTS public.concept_relationship;
DROP TABLE IF EXISTS public.concept;
DROP TABLE IF EXISTS public.relationship;
DROP TABLE IF EXISTS public.concept_class;
DROP TABLE IF EXISTS public.domain;
DROP TABLE IF EXISTS public.vocabulary;
"""

class Migration(migrations.Migration):
    dependencies = [
        ('omop', '0002_cdm_core'),  # adjust numbering to match the first file's name
    ]

    operations = [
        migrations.RunSQL(SQL_UP, reverse_sql=SQL_DOWN),
    ]
