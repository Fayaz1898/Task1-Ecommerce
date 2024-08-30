variable "region" {
  description = "The AWS region to create resources in"
  default     = "us-west-2"
}

variable "key_name" {
  description = "The key name for SSH access to EC2 instances"
  default     = "eks-keypair"
}
