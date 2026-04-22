# ### 3.8 Common Terraform Pitfalls and Mitigations 

| Pitfall | Mitigation |
|---------|------------|
| **State file corruption** from concurrent runs | Enable DynamoDB locking with `dynamodb_table`. Use S3 bucket versioning. |
| **Sensitive data in state file** | Mark outputs `sensitive = true`. Use S3 bucket encryption with KMS. Never commit `.tfstate` files. |
| **Drift between config and AWS** | Run `terraform plan` regularly in CI/CD. Use AWS Config rules. |
| **Long apply times** for EKS clusters (10-15 minutes) | Use `timeout` blocks. Break into modules. |
| **Accidental resource deletion** | Enable `prevent_destroy` lifecycle. Use `terraform plan -destroy`. |
| **Provider version mismatches** | Pin provider versions. Use Terraform lock files. |
| **DocumentDB IOPS throttling** | Set autoscaling IOPS. Use `timeouts` for operations. |
| **VPC Endpoint DNS resolution failures** | Set `private_dns_enabled = true`. Verify with `nslookup`. |
| **IRSA configuration errors** | Verify OIDC provider. Check service account annotations. |
| **EKS node group replacement** instead of update | Use `update_config` with `max_unavailable`. Separate node groups by purpose. |
