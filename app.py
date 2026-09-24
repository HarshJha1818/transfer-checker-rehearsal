import streamlit as st

st.title("Transfer Credit Gap Checker")
st.write("See which of your Florida college courses count toward your target major, and why.")

transcript = st.file_uploader("Your transcript (PDF)", type="pdf")
requirements = st.text_area("Target major requirements (paste the list)")

if st.button("Check my transfer"):
    st.subheader("Transfers")
    st.write("(coming soon)")
    st.subheader("Still needed")
    st.write("(coming soon)")
    st.subheader("Check with an advisor")
    st.write("(coming soon)")

st.info("Confirm with your academic advisor before registering.")