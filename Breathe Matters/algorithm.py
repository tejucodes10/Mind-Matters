import time
import streamlit as st
from streamlit import components

# Define program data
CLEAR_MIND_BEGINNER = {"ratio": [1, 0, 3, 0], "unit": 3, "pre": 3, "cycle": 35}
CLEAR_MIND_MEDIUM = {"ratio": [1, 0, 4, 0], "unit": 3, "pre": 3, "cycle": 28}
CLEAR_MIND_ADVANCED = {"ratio": [1, 0, 5, 0], "unit": 3, "pre": 3, "cycle": 24}
ANTI_STRESS_BEGINNER = {
    "ratio": [
        3,
        0,
        0.66,
        0],
    "unit": 3,
    "pre": 3,
    "cycle": 20}

ANTI_STRESS_MEDIUM = {
    "ratio": [
        4,
        0,
        0.66,
        0],
    "unit": 3,
    "pre": 3,
    "cycle": 17}

ANTI_STRESS_ADVANCED = {
    "ratio": [
        5,
        0,
        0.66,
        0],
    "unit": 3,
    "pre": 3,
    "cycle": 14}

ANTI_APPETITE_BEGINNER = {
    "ratio": [
        5,
        0,
        5,
        5],
    "unit": 1,
    "pre": 3,
    "cycle": 40}

ANTI_APPETITE_MEDIUM = {
    "ratio": [
        6,
        0,
        5,
        5],
    "unit": 1,
    "pre": 3,
    "cycle": 38}

ANTI_APPETITE_ADVANCED = {
    "ratio": [
        7,
        0,
        5,
        5],
    "unit": 1,
    "pre": 3,
    "cycle": 36}

DECISION_MAKING_BEGINNER = {
    "ratio": [
        5,
        2,
        7,
        0],
    "unit": 1,
    "pre": 3,
    "cycle": 6}

DECISION_MAKING_MEDIUM = {
    "ratio": [
        5,
        2,
        7,
        0],
    "unit": 1,
    "pre": 3,
    "cycle": 10}

DECISION_MAKING_ADVANCED = {
    "ratio": [
        5,
        2,
        7,
        0],
    "unit": 1,
    "pre": 3,
    "cycle": 14}

# Map step index to step name (for printing)
STEP_MAP = {0: "Inhale", 1: "Hold", 2: "Exhale", 3: "Hold"}

# Function to execute program
def execute_program(program_data):
    cycle = program_data["cycle"]
    ratio = program_data["ratio"]
    unit = program_data["unit"]
    pre = program_data["pre"]

    # Display preparation message
    st.write("Preparing...")

    for i in range(cycle):
        st.write(f"Cycle: {i + 1} (Remaining: {cycle - i - 1})")

        for index, item in enumerate(ratio):
            if item != 0:
                step_name = STEP_MAP[index]
                step_duration = unit * item

                # Display step and duration
                st.write(f"- {step_name} for {step_duration} sec")

                # Execute step (simulate duration)
                time.sleep(step_duration)

        # Display completion of cycle
        st.write("Cycle completed!")

    # Display completion message
    st.write("Program completed!")
