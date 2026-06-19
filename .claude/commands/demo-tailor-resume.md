# /demo-tailor-resume: Demo Mode: Automated Resume Build

This is a demo version of /tailor-resume. All candidate and job data is pre-loaded.
Simulate the full discovery conversation, then build and generate the tailored resume DOCX.

## Instructions

Work through every discovery question one at a time. For each question:
1. Display the question in **bold**
2. Immediately provide the pre-loaded answer in normal text, as if the user just typed it
3. Move to the next question without pausing for input

After all questions are answered, proceed through Phases 2, 3, and 4 exactly as /tailor-resume normally would: assess experience level, show the template menu, build the resume, and generate the DOCX.

For the template selection step: display the full template menu, then show Amaka selecting Template 4 Modern Tech as her choice. Then proceed to write and generate the resume.

Do not explain you are in demo mode. Just run the conversation naturally.

---

## Pre-loaded Candidate Data: Amaka Jenkins

**Q1: What role are you applying for?**
Senior Backend Engineer: Platform Infrastructure at Meridian (meridian.io). Here is the full job description:

Senior Backend Engineer: Platform Infrastructure
Company: Meridian (meridian.io) | Remote (UTC to UTC+3) | Full-time | $110,000–$140,000 USD

We are a Series B developer tools company processing 5 billion API calls per month for 800+ fintech companies. Fully remote team of 90 across 18 countries.

You will own the design and reliability of our API gateway, Kafka event streaming layer, and internal developer tooling. High-ownership role working directly with the CTO.

Required: 4+ years backend engineering, Go or Python (Go preferred), Kafka/RabbitMQ experience, PostgreSQL, AWS (ECS, RDS, Lambda), Docker, Kubernetes, strong written communication.
Nice to have: gRPC, Terraform, open-source contributions, fintech experience.
Hiring: async take-home → technical interview → CTO conversation → offer.

---

**Q2: How many years of total professional experience?**
5 years total, all full-time roles.

---

**Q3: Are you currently a student or recent graduate with limited work experience?**
No.

---

**Q4: List every role you have held.**
1. Senior Backend Engineer: Paysmart Africa, Lagos (remote), Jan 2023 to present, full-time
2. Backend Engineer: BuildStack, fully remote, Mar 2021 to Dec 2022, full-time
3. Junior Backend Developer: Techbridge Solutions, Lagos, Jun 2020 to Feb 2021, full-time

---

**Q5: For each role, the 3–5 most impactful things you did.**

Paysmart Africa (current):
- Redesigned the core payments API from a monolithic Flask app to 6 Go microservices. Response time dropped from 820ms to 260ms: 68% improvement: while supporting 3x traffic growth with no extra infrastructure
- Built a real-time fraud detection pipeline using Kafka and Redis processing 2.4 million transactions per day at sub-100ms latency, with 94% precision on suspicious activity flagging
- Migrated PostgreSQL databases to multi-region AWS RDS with read replicas, reducing query latency by 42% for users in East Africa and Europe
- Implemented GitHub Actions CI/CD cutting deployment time from 45 minutes to 8 and reducing failed deployments by 80%
- Mentored 3 junior engineers: team PR approval rate rose from 61% to 89% in 6 months

BuildStack:
- Built and maintained REST APIs serving 180,000 monthly active users using Python FastAPI and PostgreSQL
- Led Kubernetes migration from EC2, achieving 99.97% uptime and saving $40,000/year through autoscaling and right-sizing
- Designed webhook delivery system with retry logic and dead-letter queues, improving delivery success from 91% to 99.6%
- Wrote Terraform modules cutting environment setup from 3 days to 2 hours
- Parallelized test suite reducing runtime from 18 minutes to 4

Techbridge Solutions:
- Built REST APIs for HR and payroll tools used by 12 enterprise clients across Nigeria and Ghana using Django and PostgreSQL
- Integrated Flutterwave and Paystack enabling automated salary disbursement for 5,000+ employees
- Raised test coverage from 34% to 78% across 3 core service modules

---

**Q6: Highest level of education.**
BSc Computer Science, University of Lagos, Nigeria. Graduated 2020.

---

**Q7: Relevant coursework?**
Distributed Systems, Database Systems, Computer Networks, and Operating Systems: all directly relevant. Final year project was a distributed task queue system in Python benchmarked at 12,000 tasks per minute.

---

**Q8: Technical skills, tools, platforms, programming languages.**
Languages: Python, Go, SQL, Bash
Frameworks: FastAPI, Flask, Django, Gin (Go)
Databases: PostgreSQL, Redis, MongoDB
Message queues: Kafka, RabbitMQ
Cloud: AWS: EC2, RDS, Lambda, S3, ECS, CloudWatch. Some GCP.
DevOps: Docker, Kubernetes, Terraform, GitHub Actions, ArgoCD
Other: gRPC, REST, OpenAPI, JWT, OAuth2

---

**Q9: Soft skills or professional strengths.**
Strong written communication: I write RFCs and design docs and I get consistent good feedback on them. Async-first mindset. Good at explaining technical concepts to non-technical stakeholders. I enjoy mentoring and find it sharpens my own thinking.

---

**Q10: Certifications.**
- AWS Certified Developer Associate: Amazon Web Services, 2022
- Certified Kubernetes Application Developer (CKAD): CNCF, 2023

---

**Q11: Projects worth including.**
- OpenQueue: open-source distributed task queue built in Go with Redis and PostgreSQL backends. 380 GitHub stars. Supports priority queues, scheduled jobs, dead-letter handling. github.com/amaka-jenkins/openqueue
- PaySim: internal transaction simulation tool at Paysmart for load testing the payments pipeline. Used to validate the fraud detection system before launch.

---

**Q12: Volunteer experience relevant to this role.**
None.

---

**Q13: Existing resume to improve?**
No: building fresh for this role.

---

## After the conversation

Proceed through all phases of /tailor-resume:
- Assess experience level (5 years, use Professional Summary)
- Display the full template selection menu with all 8 options
- Show Amaka selecting: Template 4: Modern Tech
- Write the full tailored resume
- Generate and save the DOCX to: resume/tailored/amaka_jenkins_meridian.docx
- End with the reminder to review every line before submitting
