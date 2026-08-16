import json
import os
import streamlit as st

DB_FILE = "vocab_vault.json"

DEFAULT_DATA = {
    "akin to": ["similar to", "related to", "comparable to"],
    "similar to": ["akin to"],
    "related to": ["akin to"],
    "comparable to": ["akin to"],
    "anticipation": ["looking forward to", "expectancy"],
    "looking forward to": ["anticipation"],
    "expectancy": ["anticipation"],
    "lucid": ["crystal clear", "coherent"],
    "crystal clear": ["lucid"],
    "coherent": ["lucid"],
}


def load_data():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return DEFAULT_DATA.copy()


def save_data(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


# Streamlit Page Setup
st.set_page_config(
    page_title="Vocab Vault | Semantic Graph", page_icon="📚", layout="centered"
)

st.title("📚 Vocab Vault")
st.caption(
    "A bidirectional semantic lookup engine to map advanced synonyms and related terminology."
)

if "db" not in st.session_state:
    st.session_state.db = load_data()

db = st.session_state.db

tab_search, tab_add, tab_vault = st.tabs(
    ["🔍 Search & Lookup", "➕ Link New Words", "📖 Full Vault"]
)

with tab_search:
    st.subheader("Look Up Connections")
    query = (
        st.text_input(
            "Enter a word or phrase:",
            placeholder="e.g. akin to, similar to, lucid",
        )
        .strip()
        .lower()
    )

    if query:
        if query in db:
            st.success(f"Found connections for **'{query}'**:")
            for item in db[query]:
                st.markdown(f"- **{item}**")
        else:
            matches = [k for k in db if query in k]
            if matches:
                st.info("Exact match not found. Related terms in vault:")
                for m in matches:
                    st.markdown(f"- **{m}**")
            else:
                st.warning(
                    f"No connections found for '{query}'. Add it in the 'Link New Words' tab!"
                )

with tab_add:
    st.subheader("Create a Bidirectional Link")
    col1, col2 = st.columns(2)
    with col1:
        term1 = (
            st.text_input("First Term / Known Word", placeholder="e.g. simple")
            .strip()
            .lower()
        )
    with col2:
        term2 = (
            st.text_input(
                "Second Term / Target Word", placeholder="e.g. rudimentary"
            )
            .strip()
            .lower()
        )

    if st.button("🔗 Link Words Bidirectionally", use_container_width=True):
        if term1 and term2:
            db.setdefault(term1, [])
            db.setdefault(term2, [])

            if term2 not in db[term1]:
                db[term1].append(term2)
            if term1 not in db[term2]:
                db[term2].append(term1)

            save_data(db)
            st.session_state.db = db
            st.success(f"Successfully linked **{term1}** ⟷ **{term2}**!")
        else:
            st.error("Please fill in both terms.")

with tab_vault:
    st.subheader("Vocabulary Directory")
    st.caption(f"Total indexed terms: {len(db)}")
    for word, connections in sorted(db.items()):
        with st.expander(f"📌 {word.title()} ({len(connections)} links)"):
            for conn in connections:
                st.write(f"• {conn}")