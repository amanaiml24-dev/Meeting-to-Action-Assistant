import json

def process_transcript(transcript_text):
    lines = [line.strip() for line in transcript_text.strip().split("\n") if line.strip()]
    
    summary = []
    decisions = []
    action_items = []
    ambiguous_items = []

    for line in lines:
        line_lower = line.lower()
        if any(w in line_lower for w in ["decided", "agreed", "approved", "finalized"]):
            decisions.append(line)
        elif any(w in line_lower for w in ["will", "should", "needs to", "assigned to", "task"]):
            action_items.append(line)
            if not any(day in line_lower for day in ["by", "today", "tomorrow", "monday", "tuesday", "wednesday", "thursday", "friday", "next week"]):
                ambiguous_items.append(f"Missing Deadline: '{line}'")
        else:
            summary.append(line)

    report = {
        "Project Title": "AI-Powered Meeting-to-Action Assistant",
        "Executive Summary": summary if summary else ["Meeting transcript processed successfully."],
        "Key Decisions Made": decisions if decisions else ["No explicit decisions recorded."],
        "Assigned Action Items": action_items if action_items else ["No action items identified."],
        "Clarifications Needed (Ambiguous Items)": ambiguous_items if ambiguous_items else ["All tasks have clear deadlines."]
    }
    return report

def main():
    print("==================================================")
    print("   AI-Powered Meeting-to-Action Assistant        ")
    print("==================================================\n")

    sample_transcript = """
    Alice: Welcome everyone. We decided to launch the new dashboard next Friday.
    Bob: Great. I will prepare the user documentation.
    Charlie: Needs to review the API integration endpoints.
    Alice: Agreed, we approved the updated design mockup.
    Bob: I will handle the backend database migration.
    """

    print("--- Input Meeting Transcript ---")
    print(sample_transcript)
    print("--------------------------------\n")

    structured_output = process_transcript(sample_transcript)

    print("--- Structured Meeting Output ---")
    print(json.dumps(structured_output, indent=4))
    print("--------------------------------")

if __name__ == "__main__":
    main()