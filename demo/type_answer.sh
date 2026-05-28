#!/bin/bash
# ─────────────────────────────────────────────────────────────────
# type_answer.sh — types Amaka Jenkins's answers during the demo
#
# Usage:
#   bash demo/type_answer.sh <question_number>
#
# Run this from a second terminal (off-camera).
# You have 3 seconds after running to click into Claude Code.
# The answer will type itself at a natural human speed.
#
# Questions correspond to /tailor-resume discovery phase:
#   1  = Role applying for (just the title — paste the JD separately)
#   2  = Total years of experience
#   3  = Student or recent grad?
#   4  = List of roles
#   5a = Paysmart — impact bullets
#   5b = BuildStack — impact bullets
#   5c = Techbridge — impact bullets
#   6  = Education
#   7  = Relevant coursework
#   8  = Technical skills
#   9  = Soft skills / strengths
#   10 = Certifications
#   11 = Projects
#   12 = Volunteer experience
#   13 = Existing resume to improve?
# ─────────────────────────────────────────────────────────────────

Q=$1

case $Q in

1) TEXT="Senior Backend Engineer — Platform Infrastructure at Meridian (meridian.io). I have the full job description ready to paste." ;;

2) TEXT="5 years total. All full-time roles, no gaps. I also had a couple of short freelance API projects during university but I count from my first full-time role in June 2020." ;;

3) TEXT="No, not a student. I graduated in 2020 and have been working full-time since." ;;

4) TEXT="1. Senior Backend Engineer at Paysmart Africa — Lagos, Nigeria (remote). Jan 2023 to present. Full-time.
2. Backend Engineer at BuildStack — fully remote. Mar 2021 to Dec 2022. Full-time.
3. Junior Backend Developer at Techbridge Solutions — Lagos, Nigeria. Jun 2020 to Feb 2021. Full-time." ;;

5a) TEXT="At Paysmart, the five most impactful things I did:
- Redesigned the core payments API from a monolithic Flask app to 6 Go microservices. Response time dropped from 820ms to 260ms — a 68% improvement — and we handled 3x traffic growth with no extra infrastructure.
- Built a real-time fraud detection pipeline using Kafka and Redis. It processes 2.4 million transactions per day at sub-100ms latency and flags suspicious activity with 94% precision.
- Migrated our PostgreSQL databases to multi-region AWS RDS with read replicas, cutting query latency by 42% for users in East Africa and Europe.
- Set up GitHub Actions CI/CD that cut deployment time from 45 minutes to 8 and reduced failed deployments by 80%.
- Mentored 3 junior engineers. Team PR approval rate went from 61% to 89% in 6 months." ;;

5b) TEXT="At BuildStack:
- Built and maintained REST APIs serving 180,000 monthly active users using Python FastAPI and PostgreSQL.
- Led a Kubernetes migration from EC2 deployments. We hit 99.97% uptime and cut infrastructure spend by $40,000 per year through autoscaling and right-sizing.
- Designed a webhook delivery system with retry logic and dead-letter queues. Delivery success rate went from 91% to 99.6%.
- Wrote Terraform modules for AWS environment provisioning. Cut environment setup time from 3 days to 2 hours.
- Parallelized the test suite — runtime went from 18 minutes to 4 minutes." ;;

5c) TEXT="At Techbridge:
- Built internal REST APIs for HR and payroll tools used by 12 enterprise clients using Django and PostgreSQL.
- Integrated Flutterwave and Paystack for automated salary disbursement for over 5,000 employees.
- Raised test coverage from 34% to 78% across 3 core service modules." ;;

6) TEXT="BSc Computer Science, University of Lagos, Nigeria. Graduated 2020. Final year project was a distributed task queue system built in Python, benchmarked at 12,000 tasks per minute." ;;

7) TEXT="Yes — Distributed Systems, Database Systems, Computer Networks, and Operating Systems were all directly relevant. Distributed Systems is where I first got serious about consistency models and fault tolerance, which I use every day now." ;;

8) TEXT="Languages: Python, Go, SQL, Bash.
Frameworks: FastAPI, Flask, Django, Gin for Go.
Databases: PostgreSQL, Redis, MongoDB.
Message queues: Kafka, RabbitMQ.
Cloud: AWS — EC2, RDS, Lambda, S3, ECS, CloudWatch. Some GCP.
DevOps: Docker, Kubernetes, Terraform, GitHub Actions, ArgoCD.
Other: gRPC, REST, OpenAPI, JWT, OAuth2." ;;

9) TEXT="Strong written communication — I write detailed RFCs and design docs and I have gotten good feedback on them from senior engineers. I am also good at breaking down complex technical problems for non-technical stakeholders. Async-first mindset, which fits remote work well. And I genuinely enjoy mentoring — I find it sharpens my own understanding." ;;

10) TEXT="Two certifications:
- AWS Certified Developer Associate, issued by Amazon Web Services in 2022.
- Certified Kubernetes Application Developer (CKAD), issued by CNCF in 2023." ;;

11) TEXT="Two projects worth including:
1. OpenQueue — an open-source distributed task queue I built in Go with Redis and PostgreSQL backends. It has 380 GitHub stars and supports priority queues, scheduled jobs, and dead-letter handling. github.com/amaka-jenkins/openqueue
2. PaySim — a transaction simulation tool I built internally at Paysmart for load testing the payments pipeline. Generates realistic transaction patterns at configurable volume. Used to validate the fraud detection system before we launched it." ;;

12) TEXT="No volunteer experience directly relevant to this role." ;;

13) TEXT="No existing resume to improve — let's build it fresh for this role." ;;

*)
  echo "Unknown question number: $Q"
  echo "Valid options: 1 2 3 4 5a 5b 5c 6 7 8 9 10 11 12 13"
  exit 1
  ;;
esac

echo "Typing answer for question $Q in 3 seconds — click into Claude Code now..."
sleep 3

# Type character by character at natural human speed
python3 - << PYEOF
import subprocess, time, random

text = """$TEXT"""

for char in text:
    escaped = char.replace('\\', '\\\\').replace('"', '\\"')
    script = f'tell application "System Events" to keystroke "{escaped}"'
    subprocess.run(['osascript', '-e', script], capture_output=True)
    # Natural typing speed: 60-90ms per character with occasional pauses
    delay = random.uniform(0.055, 0.095)
    if char in '.!?,\n':
        delay += random.uniform(0.1, 0.25)
    time.sleep(delay)
PYEOF
