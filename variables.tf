variable "project" {
  type= string
  description = "This defines the name of the project"
}

variable "environment" {
  type= string
  description = "This defines the name of the environment"
}

variable "region" {
  type= string
  description = "This defines the name of region"
}


variable "domain" {
  type= string
  description = "This defines the name of this domain name"
}

variable "api_domain" {
  type= string
  description = "This defines the name of this API domain name"
}


variable "zone_id" {
  type= string
  description = "This defines the name of zone id"
}

variable "access_key" {
  type= string
}

variable "secret_key" {
  type= string
}

variable "atlas_public_key" {
  type= string
}

variable "atlas_private_key" {
  type= string
}

variable "atlas_org_id" {
  type= string
}

variable "atlas_cluster_name" {
  type= string
}

variable "atlas_project_id" {
  type= string
}

variable "mongodb_password" {
  type= string
}
