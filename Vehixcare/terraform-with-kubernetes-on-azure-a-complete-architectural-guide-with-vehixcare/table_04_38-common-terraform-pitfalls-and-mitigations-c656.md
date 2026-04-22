# ### 3.8 Common Terraform Pitfalls and Mitigations

| Pitfall | Mitigation |
|---------|------------|
| **State file corruption** from concurrent runs | Enable Azure Storage blob leases with `use_azuread_auth`. Configure `azurerm` backend with `snapshot = true`. |
| **Sensitive data in state file** (connection strings, passwords) | Mark outputs `sensitive = true`. Use `terraform state pull` for debugging only. Store state in encrypted storage account with `encryption.services.blob.enabled = true`. Never commit `.tfstate` files to Git. |
| **Drift between config and Azure** from manual changes | Run `terraform plan` regularly in CI/CD. Enable `prevent_deletion_if_contains_resources` on resource groups. Use Azure Policy to block manual changes. |
| **Long apply times** for AKS clusters (10-15 minutes) | Use `timeout` blocks on resources (`timeouts { create = "30m" }`). Break configuration into modules. Use `-parallelism=1` if hitting rate limits. |
| **Accidental resource deletion** on destroy | Enable `prevent_destroy` lifecycle on critical resources (`lifecycle { prevent_destroy = true }`). Use `terraform plan -destroy` before actual destroy. Enable soft delete on Key Vault and Cosmos DB. |
| **Provider version mismatches** across team | Pin provider versions in `required_providers`. Use Terraform lock files (`.terraform.lock.hcl`). Commit lock files to repository. |
| **Cosmos DB RU throttling** during provisioning | Set `autoscale_settings` with `max_throughput`. Use `timeouts` for create/update operations. Implement retry logic in application. |
| **Private endpoint DNS resolution failures** | Create private DNS zones with proper VNet links. Verify DNS configuration with `nslookup` from AKS nodes. Ensure `private_dns_zone_group` is configured. |
| **Terraform state secrets exposure** in CI/CD logs | Mask sensitive outputs with `echo "::add-mask::$value"`. Use Azure Key Vault for storing Terraform variables. |
| **Module version drift** | Use `ref` tags for Git modules (`source = "git::https://...?ref=v1.2.0"`). Run `terraform get -update` regularly. |
