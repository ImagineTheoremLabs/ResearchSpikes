# 📞 TheoremLabs R&D Spike — Call Handoff Strategy

## 1. Spike Overview

| Field | Entry |
| :--- | :--- |
| **Spike ID** | `SPK-010-BiDirectional-Call-Transfer` |
| **Title** | **Feasibility of Human ↔ AI Call Handoff & Context Preservation** |
| **Category** | `Telephony Engineering / AI Orchestration` |
| **Created by** | TheoremLabs Applied Innovation Labs |
| **Start Date** | *Immediate* |
| **Status** | Proposed |
| **Tags** | `ElevenLabs Client Tools`, `Native Transfer`, `SIP`, `Fastify`, `Context Handoff` |

---

## 2. Purpose & Hypothesis

### Purpose
For enterprise adoption, an AI Agent cannot be a "dead end." We need to validate the technical feasibility of **Bidirectional Transfers** using the ElevenLabs infrastructure:
1.  **AI to Human (Escalation):** The Agent detects frustration or complex intent and seamlessly transfers the call to a human operator.
2.  **Human to AI (Deflection):** A human operator transfers a routine caller to the AI Agent.

This spike requires the candidate to determine the **most native architectural pattern** for these handoffs. Does ElevenLabs provide a built-in "Transfer" function or standard tool? Or must we define a custom "Client Tool" to signal our backend?

### Hypothesis
> “ElevenLabs may provide native call control primitives (e.g., a built-in 'End Call & Patch' tool) that offer lower latency than custom webhooks. We must evaluate native capabilities first; if unavailable, we will fallback to a Custom Client Tool that signals the Fastify control plane to execute a SIP Refer or Twilio modify.”

---

## 3. Experiment / Research Method

You are responsible for designing the transfer logic. The goal is a working proof-of-concept that proves the transfer is possible and stable.

### Key Objectives

1.  **Analyze Transfer Mechanisms:**
    * **Priority A (Native Tools):** Investigate the ElevenLabs documentation and tool library. Is there a pre-built "Transfer Call" tool or system action that handles the telephony switch automatically?
    * **Priority B (Custom Tools):** If no native tool exists, implement a custom Client Tool (webhook) that the agent triggers to tell your Fastify backend to re-route the call.

2.  **Architect the Handoff Flow:**
    * Define the signaling: How does the AI know *where* to transfer? (e.g., Pre-configured department numbers vs dynamic numbers extracted from conversation).
    * **Context Passing:**  How do we send a summary of the conversation to the human agent *before* they pick up? (e.g., via SMS, Dashboard push, or Whisper).

3.  **Benchmarking:**
    * Measure the **"Dead Air" duration**: The silence between the user asking for a human and the human's phone ringing.
    * Compare the latency of Native Tools (if available) vs Custom Client Tools.

### Output Typologies

| Output Type | Expectation |
| :--- | :--- |
| **Sequence Diagram** | Visual map of the signaling flow: User Voice $\to$ AI $\to$ (Native/Custom Tool) $\to$ Telephony Transfer. |
| **Handoff Prototype** | Code or Configuration handling the transfer logic. |
| **Feasibility Report** | Assessment of latency and context preservation capabilities. |

---

## 4. Tools, Data & References

| Type | Example Entry |
| :--- | :--- |
| **Stack** | Fastify (Orchestrator), ElevenLabs ConvAI |
| **Features** | [11Labs Client Tools](https://elevenlabs.io/docs/conversational-ai/customization/client-tools), [Twilio/SIP Refer](https://www.twilio.com/docs/sip-trunking/call-transfer) |

---

## 5. Findings / Observations

Document what you discover. Some mock example findings:

- **Native Availability:** "We found a native `end_call` function but it terminates the session; it does not support transfers, so we reverted to a custom Client Tool."
- **Latency Issues:** "The AI successfully triggered the transfer tool, but there was a 3-second silence before the dial tone started."
- **Context Success:** "We successfully used the `conversation_id` to fetch the transcript and display a summary to the human agent via a WebSocket push."

Include any code snippets, screenshots, logs, or charts in `/assets/` or logs in `/notes/`.

---

## 6. Conclusion & Recommendations

| Decision | Notes |
| :--- | :--- |
| ✅ Adopt | [Your assessment on stability for production use] |
| 🔁 Iterate | [Specific improvements needed for "Dead Air" reduction] |
| 🚫 Reject | N/A |

**Recommendation:**
Provide a definitive answer: Is there a Native Tool that solves this? Or is building a custom tool the only viable path for "zero-latency" transfers?

---

## 7. Related Spikes / References
- [SPK-008: Agent Control Plane] (Where the transfer logs will be visible)
- [SPK-006: Regional Telephony Benchmark] (The telephony providers handling the actual call leg)

---

## 8. Attachments

Place any support files here:

- `/backend/` → Fastify source code (Transfer Logic & Tool definitions)
- `/diagrams/` → Call Flow Sequence Diagrams
- `/logs/` → Timing logs for Handoff latency

---

## 9. TL;DR Summary

This spike tests the "Exit Strategy" for AI calls. You will implement and validate a mechanism to **transfer calls from an AI Agent to a Human**. You must first evaluate **ElevenLabs Native Tools** for telephony control; if insufficient, you will architect a **Custom Client Tool** pattern to signal the transfer. The goal is to minimize latency and ensure context is preserved during the switch.

---

*Notes / Tips:*

- Keep each spike **bounded in time** (ideally ≤ 7 days)
- Code for **“just enough” to learn** — don’t over-engineer
- Document **failures and gaps** — they’re just as valuable
- Use clear naming: example folder name `spk-010-Call-Handoff`

Good luck!
contact author of this spike: research@theoremlabs.io
