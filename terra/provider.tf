terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = ">= 4.10.0"
    }
  }

  required_version = ">= 0.14"

  backend "gcs" {
    bucket  = "<bucket_name>"
    prefix  = "terraform/state"
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

