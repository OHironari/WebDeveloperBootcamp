#=================
# Mongo DB
#=================

# resource "mongodbatlas_project" "microblog" {
#   name   = "Microblog"
#   org_id = var.atlas_org_id
# }

# Terraform でM0は作成できない

# resource "mongodbatlas_cluster" "microblog" {
#   project_id   = mongodbatlas_project.microblog.id
#   name         = "Microblog-Application-DB"
#   cluster_type = "REPLICASET"
#   provider_name = "AWS"
#   backing_provider_name = "AWS"
#   provider_instance_size_name = "M0"
#   auto_scaling_disk_gb_enabled = true
#   mongo_db_major_version = "7.0"
#   replication_specs {
#     num_shards = 1
#     regions_config {
#       region_name     = upper(replace(var.region,"-","_"))
#       electable_nodes = 3
#       priority        = 7
#       read_only_nodes = 0
#     }
#   }
# }

resource "mongodbatlas_database_user" "microblog" {
  username           = "myuser"
  password           = var.mongodb_password
  project_id         = var.atlas_project_id
  auth_database_name = "admin"

  roles {
    role_name     = "readWriteAnyDatabase"
    database_name = "admin"
  }
}

# Current IP Address
data "http" "my_ip" {
  url = "https://api.ipify.org?format=json"
}
locals {
  my_ip = "${jsondecode(data.http.my_ip.response_body)["ip"]}/32"
}

resource "mongodbatlas_project_ip_access_list" "my_ip" {
  project_id = var.atlas_project_id
  cidr_block = local.my_ip # Replace with your IP or 0.0.0.0/0 for dev
  comment    = "Allow my IP"
}

resource "null_resource" "init_db" {
  provisioner "local-exec" {
    command = "python ./scripts/init_db.py"
  }
  depends_on = [mongodbatlas_project_ip_access_list.my_ip]
}