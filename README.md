Multi-Tenant SaaS Architecture with Schema-Based Database Isolation
===================================================================

Overview
--------

This project implements a **multi-tenant SaaS architecture** where each client gets a separate database schema. The application dynamically maps subdomains to specific schemas to ensure **data isolation and privacy**. The system is deployed on **AWS ECS**, and **GitHub Actions** handles CI/CD automation.

Architecture
------------

### Components:

1.  **Frontend (UI)** -- Web application interacting with API.
2.  **API Layer** -- Backend service managing requests, user authentication, and schema switching.
3.  **Database (PostgreSQL)** -- Single database with multiple schemas for tenant isolation.
4.  **Subdomain Routing** -- Each client has a unique subdomain (`clientA.example.com`, `clientB.example.com`), which maps to a schema.
5.  **CI/CD Pipeline (GitHub Actions + AWS ECS)** -- Automates deployment, database migrations, and scaling.

### Flow:

1.  **User Request:** UI sends a request to API.
2.  **Subdomain Detection:** Middleware extracts the subdomain.
3.  **Schema Switching:** API dynamically connects to the relevant schema.
4.  **Data Privacy Ensured:** Each client can only access their own schema.
5.  **Deployment Automation:** CI/CD pipeline ensures continuous integration and delivery.

### Problem Statement:

Design and implement CI/CD pipelines for a web service that consists of three independent components — UI, APIs, and Backend DB. The pipelines should allow:

- Deployment of the entire service or individual components as per requirement.
- Support for both default domain and user-specific subdomains.
- APIs to remain common across all deployments (packetized architecture).
- Single Database with multiple schemas, where each schema represents a different user.
- Automation of schema creation and dynamic subdomain configuration.

### Understanding:

1. The service consists of three layers:

- UI: Frontend layout that interacts with APIs.
- API: Backend APIs that perform business logic, which remains the same across all users.
- DB: A single database with multiple schemas where each schema is mapped to a unique user.

2. Deployment Requirements:

- Each component should have its own CI/CD pipeline.
- Pipelines should be capable of running independently or combined.
- Subdomains should be dynamically mapped based on user preferences.
- DB schemas should be automatically created for new users during onboarding.

3. Manual Work Identified:

- DNS Configuration for custom subdomains.
- Initial Secrets setup.
- Mapping user subdomains with API endpoints.
- DB schema creation on user onboarding.

### Approach to Solve It:

1. Separate CI/CD Pipelines:

- Create three independent pipelines for UI, API, and DB.
- Use GitHub Actions or Jenkins for pipeline automation.

2. Automating DB Schema Creation:

- Implement an API or script that automatically creates user schemas during onboarding.
- Use Alembic (Python) or Liquibase for DB migrations.

3. Subdomain Automation:

- Use cloud provider APIs like AWS Route 53 or Cloudflare to automate DNS record creation.
- Add custom pipeline steps for subdomain registration.

4. Secrets Management:

- Store sensitive information in Vault or AWS Secrets Manager.
- Automatically inject secrets during deployments.

5. API Gateway:

- Develop an API Gateway that handles subdomain registration, DB schema creation, and pipeline triggers automatically.
- The API Gateway will expose endpoints like:

-- /register-user: Accepts user data, subdomain, and schema name.
-- /trigger-pipeline: Triggers the required CI/CD pipelines.
-- /create-schema: Automates DB schema creation.

6. Pipeline YAMLs:

- Write separate GitHub Actions YAML files for UI, API, and DB pipelines.
- Design combined pipelines that sequentially trigger individual pipelines.
- Use parameters to dynamically configure subdomains and secrets during pipeline runs.
