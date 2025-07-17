# app.py
import streamlit as st
import graphviz

st.set_page_config(page_title="DFA Visualizer", layout="centered")

st.title("🧠 DFA Visualizer")

# DFA definition
states = {"q0", "q1"}
alphabet = {"0", "1"}
transitions = {
    "q0": {"0": "q0", "1": "q1"},
    "q1": {"0": "q1", "1": "q0"}
}
start_state = "q0"
accept_states = {"q0"}

# Function to draw DFA
def draw_dfa(transitions, start_state, accept_states):
    dot = graphviz.Digraph(format="png")
    dot.attr(rankdir="LR")

    for state in transitions:
        if state in accept_states:
            dot.node(state, shape="doublecircle")
        else:
            dot.node(state)

    dot.node("", shape="none")
    dot.edge("", start_state)

    for from_state, trans in transitions.items():
        for symbol, to_state in trans.items():
            dot.edge(from_state, to_state, label=symbol)

    return dot

# Display DFA
st.subheader("Defined DFA:")
st.text(f"States: {states}")
st.text(f"Alphabet: {alphabet}")
st.text(f"Start State: {start_state}")
st.text(f"Accept States: {accept_states}")

st.graphviz_chart(draw_dfa(transitions, start_state, accept_states))
