import streamlit as st
import matplotlib.pyplot as plt

st.title("CORD-19 Data Explorer")
st.write("Explore COVID-19 Research Papers Metadata")

# Year filter
min_year, max_year = int(df['year'].min()), int(df['year'].max())
year_range = st.slider("Select Year Range", min_year, max_year, (2020, 2021))

filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Show sample data
st.write(filtered.head())

# Plot publications by year
year_counts = filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
ax.set_title("Publications by Year")
st.pyplot(fig)

# Top journals
top_journals = filtered['journal'].value_counts().head(10)
st.bar_chart(top_journals)
