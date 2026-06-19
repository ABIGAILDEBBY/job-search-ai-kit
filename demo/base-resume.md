# Amaka Jenkins: Base Resume

## Contact
- Email: amaka.jenkins.dev@gmail.com
- Phone: +234 812 345 6789
- LinkedIn: linkedin.com/in/amaka-jenkins
- GitHub: github.com/amaka-jenkins
- Location: Lagos, Nigeria (fully remote)

---

## Professional Summary

Backend engineer with 5 years of experience building distributed systems and APIs for high-traffic fintech and SaaS products. Specializes in Python and Go microservices, event-driven architectures with Kafka, and cloud-native deployments on AWS. Reduced API response time by 68% at Paysmart and cut infrastructure costs by $40,000/year through a Kubernetes migration at BuildStack.

---

## Work Experience

### Senior Backend Engineer: Paysmart Africa
*Lagos, Nigeria | Remote | Jan 2023 – Present*

- Redesigned the core payments API from a monolithic Flask app to 6 Go microservices, reducing average response time from 820ms to 260ms (68% improvement) and supporting 3x traffic growth without additional infrastructure
- Built a real-time fraud detection pipeline using Kafka and Redis, processing 2.4 million transactions per day with sub-100ms latency and flagging suspicious activity with 94% precision
- Led migration of PostgreSQL databases to multi-region AWS RDS with read replicas, reducing query latency by 42% for users in East Africa and Europe
- Implemented GitHub Actions CI/CD pipeline that cut deployment time from 45 minutes to 8 minutes and reduced failed deployments by 80%
- Mentored 3 junior engineers through weekly code reviews and pair programming sessions, raising team PR approval rate from 61% to 89% in 6 months

### Backend Engineer: BuildStack
*Remote | Mar 2021 – Dec 2022*

- Built and maintained REST APIs serving 180,000 monthly active users for a developer productivity SaaS platform using Python (FastAPI) and PostgreSQL
- Led a Kubernetes migration from EC2-based deployments, achieving 99.97% uptime and reducing infrastructure spend by $40,000 per year through autoscaling and right-sizing
- Designed a webhook delivery system with retry logic and dead-letter queues, improving third-party integration reliability from 91% to 99.6% delivery success
- Wrote Terraform modules for reproducible AWS environment provisioning across staging and production, reducing environment setup time from 3 days to 2 hours
- Reduced test suite runtime from 18 minutes to 4 minutes by parallelizing pytest workers and introducing test data factories

### Junior Backend Developer: Techbridge Solutions
*Lagos, Nigeria | Jun 2020 – Feb 2021*

- Developed internal REST APIs for HR and payroll management tools used by 12 enterprise clients across Nigeria and Ghana using Django and PostgreSQL
- Integrated third-party payment gateways (Flutterwave, Paystack) into client platforms, enabling automated salary disbursement for over 5,000 employees
- Wrote unit and integration tests bringing code coverage from 34% to 78% across 3 core service modules

---

## Education

**BSc Computer Science**
University of Lagos: Lagos, Nigeria | Graduated 2020
- Final year project: Distributed task queue system built in Python, benchmarked at 12,000 tasks/minute

---

## Technical Skills

**Languages:** Python, Go, SQL, Bash
**Frameworks:** FastAPI, Flask, Django, Gin (Go)
**Databases:** PostgreSQL, Redis, MongoDB
**Message Queues:** Kafka, RabbitMQ
**Cloud:** AWS (EC2, RDS, Lambda, S3, ECS, CloudWatch), basic GCP
**DevOps:** Docker, Kubernetes, Terraform, GitHub Actions, ArgoCD
**Other:** gRPC, REST, OpenAPI, JWT, OAuth2

---

## Certifications

- AWS Certified Developer Associate: Amazon Web Services, 2022
- Certified Kubernetes Application Developer (CKAD): CNCF, 2023

---

## Projects

**OpenQueue** (github.com/amaka-jenkins/openqueue)
An open-source distributed task queue built in Go, with Redis and PostgreSQL backends. 380 GitHub stars. Supports priority queues, scheduled jobs, and dead-letter handling.

**PaySim**
A transaction simulation tool used internally at Paysmart for load testing the payments pipeline. Generates realistic transaction patterns at configurable volume, used to validate the fraud detection system before launch.
