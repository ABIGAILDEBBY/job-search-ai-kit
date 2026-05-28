# /demo-prep-interview: Demo Mode — Automated Interview Preparation

This is a demo version of /prep-interview. All candidate and job data is pre-loaded.
Simulate the input conversation, then generate the full interview preparation output.

## Instructions

Display the three input questions one at a time, immediately providing the pre-loaded answers as if the user typed them. Then run the full /prep-interview analysis and output.

Do not explain you are in demo mode. Just run it naturally.

Constraints that must be followed exactly as in /prep-interview:
- Total questions across all sections: 12 to 18. Never fewer, never more.
- No model answers. Coaching notes only.
- Output sections in order: Section 1 (resume challenge), Section 2 (technical), Section 3 (gaps — only if genuine gaps exist, otherwise omit entirely), Section 4 (role-fit).
- Every question must be traceable to a specific resume claim, JD requirement, or gap. No generic questions.

---

## Pre-loaded Data

**Q1: Paste your tailored resume.**
Amaka Jenkins | amaka.jenkins.dev@gmail.com | Lagos, Nigeria (remote) | linkedin.com/in/amaka-jenkins | github.com/amaka-jenkins

Professional Summary:
Backend engineer with 5 years of experience building high-throughput distributed systems and APIs for fintech and developer tools products. Expert in Go and Python microservices, Kafka-based event streaming, and cloud-native AWS deployments. Reduced API response time by 68% and fraud detection latency to sub-100ms at Paysmart Africa. Cut infrastructure costs by $40,000/year at BuildStack through Kubernetes migration. AWS Certified Developer and CKAD certified. Open-source contributor (OpenQueue, 380 stars).

Senior Backend Engineer — Paysmart Africa | Lagos, Nigeria (remote) | Jan 2023–Present
- Redesigned payments API from monolithic Flask to 6 Go microservices, reducing response time from 820ms to 260ms (68%) and supporting 3x traffic growth with no additional infrastructure
- Built real-time fraud detection pipeline with Kafka and Redis processing 2.4M transactions/day at sub-100ms latency with 94% precision
- Migrated PostgreSQL to multi-region AWS RDS with read replicas, reducing query latency 42% for East Africa and Europe
- Implemented GitHub Actions CI/CD cutting deployment time from 45 min to 8 min, reducing failed deployments 80%
- Mentored 3 junior engineers, raising team PR approval rate from 61% to 89% in 6 months

Backend Engineer — BuildStack | Remote | Mar 2021–Dec 2022
- Built REST APIs serving 180,000 MAU using FastAPI and PostgreSQL
- Led Kubernetes migration achieving 99.97% uptime and saving $40,000/year through autoscaling
- Designed webhook delivery system with retry logic, improving delivery success from 91% to 99.6%
- Wrote Terraform modules reducing environment setup from 3 days to 2 hours

Junior Backend Developer — Techbridge Solutions | Lagos | Jun 2020–Feb 2021
- Built REST APIs for HR and payroll tools used by 12 enterprise clients using Django and PostgreSQL
- Integrated Flutterwave and Paystack for salary disbursement covering 5,000+ employees
- Raised test coverage from 34% to 78% across 3 core modules

Education: BSc Computer Science, University of Lagos, 2020
Certifications: AWS Certified Developer Associate (2022), CKAD (2023)
Projects: OpenQueue (Go, 380 stars), PaySim (internal load testing tool)
Skills: Go, Python, PostgreSQL, Redis, Kafka, Docker, Kubernetes, Terraform, AWS, gRPC, GitHub Actions

---

**Q2: Paste the full job description.**
Senior Backend Engineer — Platform Infrastructure at Meridian (meridian.io). Remote, $110,000–$140,000.

Meridian is a Series B developer tools company processing 5 billion API calls/month for 800+ fintech companies. Fully remote, 90 people, 18 countries.

Role: Own the API gateway, Kafka event streaming layer, and internal developer tooling. High-ownership, works directly with CTO.

Required: 4+ years backend engineering, Go or Python (Go preferred), Kafka/RabbitMQ, PostgreSQL, AWS, Docker, Kubernetes, strong async written communication.
Nice to have: gRPC, Terraform, open-source contributions, fintech experience.

---

**Q3: What seniority level is this role?**
Senior.

---

## After the conversation

Run the full /prep-interview output for Amaka Jenkins applying to Meridian:
- Resume challenge questions (tied to specific bullets — the 68% latency, fraud detection numbers, the 380-star open source project)
- Technical questions (Go internals, Kafka partitioning and consumer groups, PostgreSQL indexing, Kubernetes resource management — calibrated to senior level)
- Gap questions (if any exist between her profile and the JD)
- Role-fit and behavioural questions (high ownership, async-first, mentoring, CTO-level communication)
- Readiness snapshot at the end
