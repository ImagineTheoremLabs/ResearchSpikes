
# 🧪 TheoremLabs R&D Spike Template

> Use this template for experiments (spikes) that explore technical or business hypotheses.  
> The example below walks you through evaluating **AG-UI**, an open protocol for agent–user interaction, as a possible foundation for agentic UX across frameworks.

---

## 1. Spike Overview

| Field | Entry |
|------|------|
| Spike ID | SPK-005 |
| Title | Request Resolution via Voice Agent (Refund Handling) |
| Category | Technical / Architectural Research |
| Created by | Samruddhi Ubhad, Intern |
| Start Date | 2026-02-10 |
| Status | In Progress |
| Tags | Voice Agent, Refunds, LLM, ElevenLabs, Request Resolution |

---

## 2. Purpose & Hypothesis

### Purpose

Customer support teams frequently handle refund-related calls, which are repetitive, policy-driven, and time-consuming. 
This spike explores whether a voice-based AI agent can autonomously manage end-to-end refund resolution while maintaining policy compliance, auditability, and acceptable latency.

The objective is to design and validate a minimal Proof of Concept (PoC) voice agent that can:

- Authenticate a customer securely
- Retrieve order and transaction history
- Apply refund eligibility policies
- Execute a refund when criteria are met
- Generate auditable artifacts (decision log, transcript, receipt)

The spike focuses on feasibility, architectural clarity, and cost visibility rather than production readiness.

---

### Hypothesis

> With a lightweight toolset for identity verification, data retrieval, and policy enforcement, a voice-based LLM agent can autonomously resolve common refund requests while reducing average handling time and producing structured, auditable outputs.


---

## 3. Experiment / Research Method

### Objectives

1. Validate whether a voice-based LLM agent can securely authenticate a caller.
2. Test retrieval of order and transaction history from structured data.
3. Evaluate policy-based refund decision logic.
4. Simulate refund execution and receipt generation.
5. Measure feasibility in terms of latency, architectural complexity, and cost per resolution.

---

### Experimental Steps

#### Step 1 — Define Test Data & Policies

- Create mock customer records with:
  - Order ID
  - Order date
  - Payment method
  - Delivery status
- Define refund rules:
  - 30-day eligibility window
  - Item must be delivered
  - No refund for promotional clearance items
- Prepare two test scenarios:
  - Eligible refund case
  - Ineligible refund case

---

#### Step 2 — Design Voice Interaction Flow

Minimal conversational flow:

1. Customer provides order ID and email/phone.
2. Agent verifies identity.
3. Agent retrieves order history.
4. Agent evaluates refund eligibility.
5. Agent responds with approval or denial.
6. Agent generates confirmation details.

Focus on short, controlled conversation turns to reduce latency.

---

#### Step 3 — Implement Core Logic (Mocked Backend)

Instead of integrating real payment gateways, simulate:

- `verifyIdentity()`
- `fetchOrderHistory()`
- `evaluateRefundPolicy()`
- `executeRefund()`

All outputs should generate a structured decision log.

---

#### Step 4 — Artifact Generation

For each test run, generate:

- Structured decision log (JSON-style)
- Simulated refund receipt
- Transcript text file
- Cost estimation snapshot

---

#### Step 5 — Evaluation Metrics

Measure:

- Authentication success
- Correctness of refund decision
- Logical consistency
- Estimated cost per resolution
- Feasibility of scaling to real systems

---

## 4. Tools, Data & References

| Type | Description |
|------|------------|
| Voice Agent Runtime | ElevenLabs Conversational AI (preferred) or equivalent LLM-backed voice interface |
| LLM Engine | OpenAI GPT-style model for reasoning, intent classification, and policy evaluation |
| Backend Simulation | Mock service functions to simulate identity verification, order lookup, and refund execution |
| Data Fixtures | Sample customer records with order history and payment details |
| Storage | Local JSON logs for decision logs, transcript files, and simulated refund receipts |
| Policy Logic | Rule-based eligibility function (30-day window, delivery confirmation, exclusions) |
| Metrics Tracking | Manual logging of latency, decision accuracy, and cost estimation |
| References | TheoremLabs Spike Brief (SPK-005), ElevenLabs Docs, LLM architecture patterns |


---

## 5. Findings / Observations

### Identity & Authentication

Using structured identity verification (Order ID + email/phone confirmation) is sufficient for low-risk refund flows. 
However, stronger verification (OTP to registered contact) would be required for higher refund amounts or fraud-sensitive scenarios.

Voice-based identity collection increases friction slightly but remains acceptable for simple flows.

---

### Policy Evaluation Logic

Rule-based refund policies (e.g., 30-day window + delivery confirmation) are straightforward to evaluate using structured data. 
LLM reasoning is helpful for interpreting edge-case user statements (e.g., unclear return reasons), but core eligibility should remain deterministic and rule-driven.

Separation of policy logic from conversational logic improves system reliability.

---

### Latency & Flow Design

Short conversational turns reduce perceived latency. 
The longest delay occurs during simulated order lookup and policy evaluation. 
In a real implementation, backend API response time would directly impact user experience.

Streaming responses can improve perceived responsiveness.

---

### Auditability & Logging

Structured decision logs significantly improve traceability. 
Generating a JSON-style decision record (including policy version and decision reason) makes the system audit-friendly and compliance-ready.

Transcript storage is necessary for quality review and dispute resolution.

---

### System Limitations Identified

- Fraud detection mechanisms were not implemented in this PoC.
- Escalation to a human agent was not simulated.
- Real payment gateway integration was intentionally mocked.
- Complex refund scenarios (partial refunds, promotional adjustments) require additional logic layers.

---
## 6. Cost Model (Simple)

To estimate feasibility, we approximate the per-resolution cost of a refund handled by a voice-based LLM agent.

Let:

- C_voice = Voice runtime + LLM cost per minute  
- C_tel = Optional telephony cost per minute  
- C_tx = Transaction or refund processing cost  
- C_store = Storage cost for transcript and decision logs  
- M = Average minutes per resolved request  

### Estimated Cost Formula

Cost per resolution ≈ M × (C_voice + C_tel) + C_tx + C_store

---

### Assumptions for PoC

- Average handling time: 4–6 minutes  
- LLM usage concentrated during authentication and policy evaluation  
- Mock backend has negligible cost  
- Storage cost is minimal for compressed transcript + JSON logs  

---

### Observations

- Reducing conversational length directly reduces cost.  
- Keeping policy evaluation deterministic avoids unnecessary LLM tokens.  
- Streaming short confirmations improves user experience without increasing cost significantly.  
- For high call volumes, cost predictability becomes critical.  

In a scaled deployment, monitoring average handling time (AHT) is the primary lever for cost control.

## 7. Conclusion & Recommendations

This spike demonstrates that a voice-based LLM agent can feasibly handle structured refund resolution workflows under controlled policy constraints.

The PoC validates that:

- Identity verification can be handled using structured inputs.
- Refund eligibility logic should remain rule-based for reliability.
- LLM reasoning is most useful for conversational flow and edge-case interpretation.
- Structured decision logs significantly improve auditability.
- Cost is directly tied to conversation length and backend latency.

### Recommendation

Proceed with a controlled pilot implementation using:

- Deterministic policy enforcement
- Mocked backend replaced by real read-only integrations
- Refund execution behind feature flags
- Escalation pathways for complex or fraud-sensitive cases

Future iterations should incorporate:

- OTP-based verification
- Fraud scoring integration
- Partial refund logic
- CRM writeback
- Real-time monitoring dashboards

Overall, the architecture is feasible and scalable for common refund scenarios, provided that compliance and cost controls are enforced from the outset.


## 7. Related Spikes / References

- AG-UI GitHub & docs: https://github.com/ag-ui-protocol/ag-ui  

---

## 8. Attachments

Place any support files here:

- `/assets/` → UI screenshots, interaction diagrams  
- `/code/` → adapter modules, demo frontend/backends  
- `/logs/` → performance logs, profiling outputs  

---

## 9. TL;DR Summary

This spike evaluated **AG-UI** as a vendor-agnostic UI protocol for agentic applications. We built adapters for LangChain and CrewAI, tested streaming, state sync, and error recovery. While AG-UI accelerated UI integration across frameworks, we ran into performance overhead and minor protocol gaps (e.g. lack of “partial update” event). I recommend a pilot adoption path with iterative connector improvements.

---

*Notes / Tips:*

- Keep each spike **bounded in time** (ideally ≤ 7 days)  
- Code for **“just enough” to learn** — don’t over-engineer  
- Document **failures and gaps** — they’re just as valuable  
- Use clear naming: example folder name `spk-007-ag-ui-evaluation`

Good luck! Let me know if you’d like a companion **`submission-guide.md`** tuned for AG-UI spike submissions.
::
```
