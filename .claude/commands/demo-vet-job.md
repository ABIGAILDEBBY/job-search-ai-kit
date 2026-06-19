# /demo-vet-job: Demo Mode: Automated Job Audit

This is a demo version of /vet-job. All candidate and job data is pre-loaded.
Run the full audit automatically without waiting for user input.

## Instructions

Simulate the conversation naturally. For each question you would normally ask, display it clearly, then immediately provide the answer from the pre-loaded data below as if the user just typed it. Add a natural transition between question and answer (e.g. a line break). Then proceed to the audit.

Keep the simulation clean: show the question in **bold**, then the answer in normal text, then move on. Do not explain that you are in demo mode mid-conversation. Just run it.

---

## Pre-loaded Data

**Candidate:** Amaka Jenkins
**Location:** Lagos, Nigeria
**Work authorization:** Fully remote only, no sponsorship needed

**Job description to audit:**

Senior Backend Engineer: Platform Infrastructure
Company: Meridian (meridian.io)
Location: Remote (UTC to UTC+3 preferred)
Type: Full-time
Salary: $110,000 – $140,000 USD
Posted: 3 days ago

About Meridian:
Meridian is a Series B developer tools company building the infrastructure layer for real-time financial data. Our platform processes over 5 billion API calls per month for 800+ fintech companies worldwide. We are a fully remote team of 90 people across 18 countries and have been remote-first since founding.

The Role:
We are looking for a Senior Backend Engineer to join our Platform Infrastructure team. You will own the design and reliability of the core API gateway, event streaming layer, and internal developer tooling that every Meridian product is built on. This is a high-ownership role: you will work directly with the CTO and make architectural decisions that affect every team.

What You Will Do:
- Design, build, and maintain high-throughput backend services in Go handling millions of requests per day
- Own the reliability and scalability of our Kafka-based event streaming infrastructure
- Lead architectural decisions for new platform features and document trade-offs clearly
- Collaborate with product and frontend teams to design clean, versioned APIs
- Contribute to and improve our Kubernetes-based deployment infrastructure on AWS
- Mentor mid-level engineers through code reviews, design discussions, and pairing
- Participate in on-call rotation (compensated, well-structured runbooks, low noise)

Required:
- 4+ years of backend engineering experience with production systems at scale
- Strong proficiency in Go or Python (Go strongly preferred)
- Deep experience with event-driven architectures and message queues (Kafka, RabbitMQ, or similar)
- Solid PostgreSQL skills: query optimization, indexing, and schema design
- Experience deploying and operating services on AWS (ECS, RDS, Lambda, or equivalent)
- Comfort with Docker and Kubernetes in production
- Strong written communication: async-first culture

Nice to Have:
- Experience with gRPC or GraphQL
- Familiarity with Terraform or other IaC tools
- Open-source contributions
- Experience in fintech or developer tools

Compensation:
- $110,000 – $140,000 base salary (location-independent)
- Equity: 0.05% – 0.15%
- $3,000/year home office stipend
- $2,000/year L&D budget
- 35 days PTO
- No visa sponsorship required: hires globally via Deel/Remote

Hiring process: async take-home (2 hours) → technical interview (90 min) → CTO conversation (45 min) → offer.

---

## Simulation Format

Display this exchange first:

**"Please paste the full job description, or share the URL."**
Senior Backend Engineer: Platform Infrastructure at Meridian (meridian.io). Pasting the full JD now.
[paste the job description above]

**"What draws you to this role specifically?"**
Meridian processes 5 billion API calls a month: the scale is real. The role owns the API gateway and event streaming layer which is exactly the kind of infrastructure work I have been doing at Paysmart. And they are remote-first with no timezone restrictions, which matters a lot to me as someone based in Lagos.

**"Have you already researched this company at all?"**
A little. I know they are Series B and remote-first since founding. I have not gone deep on the team or engineering blog yet: that is what I want to do before I decide whether to apply.

---

Then run the full /vet-job audit using that job description and Amaka's profile. Complete all 7 steps. End with a clear recommendation.
