# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 23:02:25 2024

@author: MSI
"""

pink_color = "#f63366"
black_color = "#000000"
white_color = "#FFFFFF"
# Import sqlite3 and pandas
import sqlite3
import pandas as pd
import streamlit as st
st.set_page_config(page_title="Blogging Matters", page_icon=":)", layout="centered", initial_sidebar_state="expanded")
# Connect to the database
conn = sqlite3.connect('blog.db')
c = conn.cursor()

# Create a table if not exists
c.execute('CREATE TABLE IF NOT EXISTS posts (author TEXT NOT NULL, title TEXT NOT NULL, content TEXT NOT NULL, date DATE NOT NULL)')

# Close the connection and the cursor
conn.close()


# Define a function to add a new post
def add_post(author, title, content, date):
    try:
        # Connect to the database
        conn = sqlite3.connect('blog.db')
        c = conn.cursor()
        # Insert a new row into the posts table
        c.execute('INSERT INTO posts (author, title, content, date) VALUES (?,?,?,?)', (author, title, content, date))
        # Save the changes to the database
        conn.commit()
    except sqlite3.Error as e:
        # Print the error message
        print(e)
    finally:
        # Close the connection and the cursor
        conn.close()

# Define a function to get all the posts
def get_all_posts():
    try:
        # Connect to the database
        conn = sqlite3.connect('blog.db')
        c = conn.cursor()
        # Select all the rows from the posts table
        c.execute('SELECT * FROM posts')
        # Fetch all the results
        data = c.fetchall()
        return data
    except sqlite3.Error as e:
        # Print the error message
        print(e)
    finally:
        # Close the connection and the cursor
        conn.close()

# Define a function to get a post by title
def get_post_by_title(title):
    try:
        # Connect to the database
        conn = sqlite3.connect('blog.db')
        c = conn.cursor()
        # Select the row from the posts table that matches the title
        c.execute('SELECT * FROM posts WHERE title=?', (title,))
        # Fetch the result
        data = c.fetchone()
        return data
    except sqlite3.Error as e:
        # Print the error message
        print(e)
    finally:
        # Close the connection and the cursor
        conn.close()

# Define a function to delete a post
def delete_post(title):
    try:
        # Connect to the database
        conn = sqlite3.connect('blog.db')
        c = conn.cursor()
        # Delete the row from the posts table that matches the title
        c.execute('DELETE FROM posts WHERE title=?', (title,))
        # Save the changes to the database
        conn.commit()
    except sqlite3.Error as e:
        # Print the error message
        print(e)
    finally:
        # Close the connection and the cursor
        conn.close()

# Create a sidebar menu with different options
menu = ["Home", "View Posts", "Add Post", "Search", "Manage"]
choice = st.sidebar.selectbox("Menu", menu)

# Display the selected option
if choice == "Home":
    st.markdown(f"""
    <div style="background-color:{pink_color};padding:3px;border-radius:3px">
    <h1 style="color:{white_color};text-align:center;">BLOGGING MATTERS</h1>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="background-color:{black_color};padding:3px;border-radius:3px">
    <h1 style="color:{white_color};text-align:center;">Your safe space</h1>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("")
    st.write("Our blog provides a safe haven for individuals to openly express their thoughts and feelings on mental health issues, free from judgment or stigma. In this digital sanctuary, we invite people to share their experiences and find support in a community that understands and empathizes with their struggles, fostering understanding and destigmatizing discussions one story at a time.")
    st.write("Blogging Matters offers a menu, granting users the convenience to effortlessly navigate through viewing, adding, searching, and managing posts. Enjoy seamless access to a suite of functionalities designed to streamline your blogging experience, ensuring efficiency and ease every step of the way.")
    

elif choice == "View Posts":
    st.title("View Posts")
    st.write("Scroll to see all posts on 'Blogging Matters'")
    # Get all the posts from the database
    posts = get_all_posts()
    # Display each post in a card layout
    for post in posts:
        st.markdown(
            f"""
            <div style="border: 1px solid #ccc; border-radius: 5px; padding: 10px; margin-bottom: 10px;">
                <h3>{post[1]}</h3>
                <p><strong>Author:</strong> {post[0]}</p>
                <p><strong>Date:</strong> {post[3]}</p>
                <p>{post[2]}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

elif choice == "Add Post":
    st.title("Add Post")
    st.write("Add a new post to the blogging platfor")
    # Create a form to get the post details
    with st.form(key="add_form"):
        author = st.text_input("Author")
        title = st.text_input("Title")
        content = st.text_area("Content")
        date = st.date_input("Date")
        submit = st.form_submit_button("Submit")
    # If the form is submitted, add the post to the database
    if submit:
        add_post(author, title, content, date)
        st.success("Post added successfully")

elif choice == "Search":
    st.title("Search")
    st.write("Here you can search for a post by title or author.")
    # Create a text input to get the search query
    query = st.text_input("Enter your search")
    # If the query is not empty, search for the matching posts
    if query:
        # Get all the posts from the database
        posts = get_all_posts()
        # Filter the posts by the query
        results = [post for post in posts if query.lower() in post[0].lower() or query.lower() in post[1].lower()]
        # Display the results
        if results:
            st.write(f"Found {len(results)} matching posts:")
            for result in results:
                st.markdown(
                    f"""
                    <div style="border: 1px solid #ccc; border-radius: 5px; padding: 10px; margin-bottom: 10px;">
                        <h3>{result[1]}</h3>
                        <p><strong>Author:</strong> {result[0]}</p>
                        <p><strong>Date:</strong> {result[3]}</p>
                        <p>{result[2]}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        else:
            st.write("No matching posts found")

elif choice == "Manage":
    st.title("Manage")
    st.write("View insights or delete posts")
    # Create a selectbox to choose a post to delete
    titles = [post[1] for post in get_all_posts()]
    title = st.selectbox("Select a post to delete", titles)
    # Add a button to confirm the deletion
    if st.button("Delete"):
        delete_post(title)
        st.success("Post deleted successfully")
    # Create a checkbox to show some statistics
    if st.checkbox("Show statistics"):
        # Get all the posts from the database
        posts = get_all_posts()
        # Convert the posts to a dataframe
        df = pd.DataFrame(posts, columns=["author", "title", "content", "date"])
        # Display some basic statistics
        st.write("Number of posts:", len(posts))
        st.write("Number of authors:", len(df["author"].unique()))
        st.write("Most recent post:", df["date"].max())
        st.write("Oldest post:", df["date"].min())
        # Display a bar chart of posts by author
        st.write("Posts by author:")
        author_count = df["author"].value_counts()
        st.bar_chart(author_count)
