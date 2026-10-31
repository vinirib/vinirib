<h1 align="center">Hi, I'm Vinícius Ribeiro 👋</h1>

<p align="center">
  <a href="https://github.com/vinirib"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=20&duration=2800&pause=900&color=4F46E5&center=true&vCenter=true&width=520&lines=Backend+engineer;Distributed+systems+%26+APIs;Go+%C2%B7+Java+%C2%B7+Python+%C2%B7+TypeScript;AI-assisted+engineering" alt="Backend engineer, distributed systems and APIs, Go, Java, Python, TypeScript, AI-assisted engineering"/></a>
</p>

<p align="center">
  <b>Senior Backend Engineer</b> · distributed systems and APIs · AI-assisted engineering<br/>
  10+ years shipping backend in production · São Paulo 🇧🇷 · remote
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/viniciusribeirosp/"><img src="https://img.shields.io/badge/LinkedIn-viniciusribeirosp-4F46E5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <a href="mailto:viniciusribeirosp@gmail.com"><img src="https://img.shields.io/badge/Email-get%20in%20touch-4F46E5?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>
  <a href="https://github.com/vinirib?tab=followers"><img src="https://img.shields.io/github/followers/vinirib?style=for-the-badge&logo=github&label=Follow&color=4F46E5" alt="Follow @vinirib"/></a>
  <img src="https://komarev.com/ghpvc/?username=vinirib&style=for-the-badge&color=4F46E5&label=Profile+views" alt="Profile views"/>
</p>

---

## 👋 About

I build backend systems that other systems depend on. I care about clean API contracts, failures that are safe to retry, and code the next person can read. I pick the language that fits the problem, not the other way around.

- 🧩 **Distributed systems and APIs:** event driven, contract first, idempotent, observable
- 🤖 **AI-assisted engineering:** agents that work with real context and get checked by real tests
- 🛠️ **Open source:** fixing and improving the libraries I use every day

---

## 🧠 How I use AI

- **Context engineering.** Versioned knowledge, architecture patterns and reusable Claude Code Skills, so the agent works from real context instead of guesses.
- **Verification first.** The AI drafts. Tests, contracts and a human review decide what ships.

![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=claude&logoColor=white)
![GitHub Copilot](https://img.shields.io/badge/GitHub_Copilot-000000?style=flat-square&logo=githubcopilot&logoColor=white)
![ChatGPT](https://img.shields.io/badge/ChatGPT%20%2F%20Codex-412991?style=flat-square&logo=openai&logoColor=white)

---

## 🌱 Open source right now

<!-- OSS-PROJECTS:START -->
| Project | What it is | What I'm doing |
|---------|------------|----------------|
| **[idempotency4j](https://github.com/josipmusa/idempotency4j)** | Run a unit of work at most once per key and replay the stored result | Storage policies, Retry-After handling, Spring Boot wiring. 5 PRs merged |
| **[idempotence4j](https://github.com/transferwise/idempotence4j)** | Wise's library for idempotent actions | Spring Web module, payload mismatch detection, Java 21/25 build |
| **[swagger-parser](https://github.com/swagger-api/swagger-parser)** | The OpenAPI parser behind most of the Swagger tooling | OpenAPI 3.1 `$ref` resolution fixes, JDK 21/25 CI |
| **[floci](https://github.com/floci-io/floci)** | Free, fast local AWS emulator | CloudFront custom origin and Cognito CloudFormation MFA fixes. 3 PRs merged |
| **[clauditor](https://github.com/IyadhKhalfallah/clauditor)** | Session and quota tool for Claude Code | Memory crash fix at session start, CI security audit fix |
| **[claude-mem](https://github.com/thedotmack/claude-mem)** | Persistent memory for coding agents | Folder CLAUDE.md and search date bound fixes |
| **[openapi-generator](https://github.com/OpenAPITools/openapi-generator)** | Generates clients and servers from OpenAPI specs | Java/Spring generator fixes |
| **[opensearch-java](https://github.com/opensearch-project/opensearch-java)** | The official Java client for OpenSearch | Thread safety fix in JSON deserialization |
| **[pact-jvm](https://github.com/pact-foundation/pact-jvm)** | Consumer-driven contract testing for the JVM | Consumer DSL fixes and issue triage |
| **[quarkus](https://github.com/quarkusio/quarkus)** | Quarkus: Supersonic Subatomic Java. | First PRs in review |
<!-- OSS-PROJECTS:END -->

**Latest pull requests**

<!-- OSS-PRS:START -->
- 🟢 **thedotmack/claude-mem** [#5238](https://github.com/thedotmack/claude-mem/pull/5238) fix(chroma): do not re-embed unchanged documents on a duplicate conflict (#5237)
- 🟢 **opensearch-project/opensearch-java** [#2254](https://github.com/opensearch-project/opensearch-java/pull/2254) Fix a race in ArrayDeserializer.acceptedEvents()
- 🟢 **quarkusio/quarkus** [#57979](https://github.com/quarkusio/quarkus/pull/57979) Log Maven settings warnings without a stack trace
- 🟣 **floci-io/floci** [#7088](https://github.com/floci-io/floci/pull/7088) fix(cloudformation): keep SMS_MFA on a user pool update until MFA is turned off
- 🟢 **thedotmack/claude-mem** [#5234](https://github.com/thedotmack/claude-mem/pull/5234) fix(search): read an all-digit dateStart/dateEnd as epoch ms (#5233)
- 🟢 **IyadhKhalfallah/clauditor** [#153](https://github.com/IyadhKhalfallah/clauditor/pull/153) fix(hooks): deliver SessionStart context through hookSpecificOutput
<!-- OSS-PRS:END -->

---

## 🛠️ Tech stack

<p>
  <img src="https://skillicons.dev/icons?i=go,java,kotlin,py,ts,spring,fastapi,kafka,postgres,redis,aws,kubernetes,docker,terraform&perline=14" alt="Go, Java, Kotlin, Python, TypeScript, Spring, FastAPI, Kafka, PostgreSQL, Redis, AWS, Kubernetes, Docker, Terraform"/>
</p>

| Area | Technologies |
|------|--------------|
| **Languages** | Go, Java, Kotlin, Python, TypeScript, SQL |
| **Frameworks** | Spring Boot, FastAPI, Node.js, Go standard library |
| **APIs & messaging** | REST, OpenAPI, GraphQL, gRPC, Kafka, RabbitMQ |
| **Data** | PostgreSQL, Redis, MongoDB, Oracle |
| **Cloud & infra** | AWS, GCP, Kubernetes, Docker, Helm, ArgoCD, Terraform |
| **Testing** | Testcontainers, JUnit, Go test, Pytest, Pact |
| **Observability** | Datadog, Grafana, Prometheus, OpenTelemetry |

---

## 📌 Earlier work worth a look

- **[zup-pact-workshop](https://github.com/vinirib/zup-pact-workshop)**: hands-on consumer driven contract testing workshop with Pact, used to train dozens of engineers.
- **[pact-ci-workshop](https://github.com/vinirib/pact-ci-workshop)**: contract tests wired into a CI pipeline, from broker to `can-i-deploy`.
- **[pact-consumer-sample](https://github.com/vinirib/pact-consumer-sample)** / **[pact-provider-sample](https://github.com/vinirib/pact-provider-sample)**: the smallest working consumer and provider pair.

---

## 📊 Stats

<p align="center">
  <img src="metrics/stats.svg" alt="GitHub stats and languages"/>
</p>
<p align="center">
  <img src="metrics/calendar.svg" alt="Contribution calendar and streak"/>
</p>

---

## 📬 Find me

<p>
  <a href="https://www.linkedin.com/in/viniciusribeirosp/"><img src="https://img.shields.io/badge/LinkedIn-viniciusribeirosp-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <a href="mailto:viniciusribeirosp@gmail.com"><img src="https://img.shields.io/badge/Email-viniciusribeirosp%40gmail.com-c14438?style=flat-square&logo=gmail&logoColor=white" alt="Email"/></a>
  <a href="https://github.com/vinirib"><img src="https://img.shields.io/badge/GitHub-vinirib-181717?style=flat-square&logo=github" alt="GitHub"/></a>
</p>

<p align="center">
  <sub>☕ Coffee, clean APIs and well-tested contracts.</sub>
</p>
