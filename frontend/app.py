# import streamlit as st
# import requests
# import plotly.graph_objects as go

# # ---------------------------------
# # PAGE CONFIG
# # ---------------------------------

# st.set_page_config(
#     page_title="LeadGPT",
#     layout="wide"
# )

# # ---------------------------------
# # SIDEBAR
# # ---------------------------------

# st.sidebar.title("LeadGPT")
# st.sidebar.info("AI Lead Intelligence Platform")

# page = st.sidebar.selectbox(
#     "Navigation",
#     ["Dashboard", "Forecasting", "AI Insights", "RAG Chatbot"]
# )

# # ---------------------------------
# # DASHBOARD PAGE
# # ---------------------------------

# if page == "Dashboard":

#     st.title("LeadGPT Dashboard")

#     # KPI CARDS

#     col1, col2, col3 = st.columns(3)

#     col1.metric("Total Leads", "7,422")
#     col2.metric("Model Accuracy", "76%")
#     col3.metric("ROC-AUC", "0.84")

#     st.divider()

#     st.header("Lead Prediction")

#     product_id = st.text_input("Product ID")

#     source = st.selectbox(
#         "Lead Source",
#         ["Referral", "Website", "Call", "Live Chat"]
#     )

#     mobile = st.text_input("Mobile Number")
#     email = st.text_input("Email")

#     sales_agent = st.text_input("Sales Agent")
#     location = st.text_input("Location")

#     delivery_mode = st.selectbox(
#         "Delivery Mode",
#         ["Online", "Offline"]
#     )

#     day = st.number_input("Day", min_value=1, max_value=31)
#     month = st.number_input("Month", min_value=1, max_value=12)
#     hour = st.number_input("Hour", min_value=0, max_value=23)
#     weekday = st.number_input("Weekday", min_value=0, max_value=6)

#     weekend = st.selectbox("Weekend", [0, 1])
#     has_mobile = st.selectbox("Has Mobile", [0, 1])
#     valid_email = st.selectbox("Valid Email", [0, 1])

#     if st.button("Predict Lead Quality"):

#         payload = {
#             "Product_ID": product_id,
#             "Source": source,
#             "Mobile": mobile,
#             "EMAIL": email,
#             "Sales_Agent": sales_agent,
#             "Location": location,
#             "Delivery_Mode": delivery_mode,

#             "Created_Day": day,
#             "Created_Month": month,
#             "Created_Hour": hour,
#             "Created_Weekday": weekday,

#             "Is_Weekend": weekend,

#             "Has_Mobile": has_mobile,
#             "Valid_Email": valid_email
#         }

#         response = requests.post(
#             "http://127.0.0.1:8000/predict",
#             json=payload
#         )

#         result = response.json()

#         prediction = result["prediction"]
#         probability = result["probability"]

#         st.success(f"Prediction: {prediction}")

#         # ---------------------------------
#         # PROBABILITY CHART
#         # ---------------------------------

#         fig = go.Figure(go.Indicator(
#             mode="gauge+number",
#             value=probability * 100,
#             title={'text': "Conversion Probability"},
#             gauge={
#                 'axis': {'range': [0, 100]}
#             }
#         ))

#         st.plotly_chart(fig)

#         # # ---------------------------------
#         # # SHAP EXPLAINABILITY
#         # # ---------------------------------

#         # st.subheader("Prediction Explanation")

#         # shap_response = requests.post(
#         #     "http://127.0.0.1:8000/shap",
#         #     json=payload
#         # )

#         # shap_result = shap_response.json()

#         # st.write(shap_result)


# # ---------------------------------
# # AI INSIGHTS PAGE
# # ---------------------------------

# if page == "AI Insights":

#     st.title("AI Business Insights")

#     prompt = st.text_area(
#         "Ask Business Question"
#     )

#     if st.button("Generate Insight"):

#         response = requests.post(
#             "http://127.0.0.1:8000/insight",
#             json={"prompt": prompt}
#         )

#         result = response.json()

#         st.info(result["insight"])


# # ---------------------------------
# # FORECASTING PAGE
# # ---------------------------------

# if page == "Forecasting":

#     st.title("Lead Forecasting")

#     st.subheader("30-Day Lead Forecast")

#     response = requests.get(
#         "http://127.0.0.1:8000/forecast"
#     )

#     forecast_data = response.json()

#     import pandas as pd

#     forecast_df = pd.DataFrame(forecast_data)

#     # ---------------------------------
#     # FORECAST CHART
#     # ---------------------------------

#     fig = go.Figure()

#     fig.add_trace(
#         go.Scatter(
#             x=forecast_df["ds"],
#             y=forecast_df["yhat"],
#             mode="lines+markers",
#             name="Forecast"
#         )
#     )

#     fig.update_layout(
#         title="Future Lead Forecast",
#         xaxis_title="Date",
#         yaxis_title="Predicted Leads"
#     )

#     st.plotly_chart(fig, use_container_width=True)

#     st.dataframe(forecast_df)
# # ---------------------------------
# # RAG CHATBOT PAGE
# # ---------------------------------

# if page == "RAG Chatbot":

#     st.title("LeadGPT Business Assistant")

#     st.subheader("Ask Questions About Sales & Leads")

#     # =========================================
#     # CUSTOM STYLING
#     # =========================================

#     st.markdown(
#         """
#         <style>

#         .chat-container {
#             background-color: #1e1e1e;
#             padding: 25px;
#             border-radius: 15px;
#             border: 1px solid #333333;
#             margin-top: 20px;
#             margin-bottom: 20px;
#         }

#         .answer-text {
#             color: white;
#             font-size: 17px;
#             line-height: 1.8;
#             white-space: pre-wrap;
#         }

#         .info-card {
#             background-color: #262730;
#             padding: 15px;
#             border-radius: 10px;
#             text-align: center;
#             color: white;
#             border: 1px solid #3a3a3a;
#         }

#         </style>
#         """,
#         unsafe_allow_html=True
#     )

#     # =========================================
#     # USER INPUT
#     # =========================================

#     question = st.text_area(
#         "Enter your business question",
#         height=120,
#         placeholder="Example: Which sales agent appears most frequently?"
#     )

#     # =========================================
#     # ASK AI BUTTON
#     # =========================================

#     if st.button("Ask AI"):

#         if question.strip() == "":
#             st.warning("Please enter a business question.")

#         else:

#             with st.spinner("LeadGPT is analyzing business records..."):

#                 try:

#                     # =========================================
#                     # API CALL
#                     # =========================================

#                     response = requests.post(
#                         "http://127.0.0.1:8000/rag",
#                         json={
#                             "question": question
#                         }
#                     )

#                     result = response.json()

#                     answer = result.get("answer", "No response received.")

#                     documents_found = result.get("documents_found", 0)

#                     status = result.get("status", "unknown")

#                     # =========================================
#                     # MAIN RESPONSE CARD
#                     # =========================================

#                     st.markdown("## LeadGPT Analysis")

#                     st.markdown(
#                         f"""
#                         <div class="chat-container">
#                             <div class="answer-text">
#                                 {answer}
#                             </div>
#                         </div>
#                         """,
#                         unsafe_allow_html=True
#                     )

#                     # =========================================
#                     # METRICS SECTION
#                     # =========================================

#                     col1, col2 = st.columns(2)

#                     with col1:
#                         st.markdown(
#                             f"""
#                             <div class="info-card">
#                                 <h4>Documents Retrieved</h4>
#                                 <h2>{documents_found}</h2>
#                             </div>
#                             """,
#                             unsafe_allow_html=True
#                         )

#                     with col2:
#                         st.markdown(
#                             f"""
#                             <div class="info-card">
#                                 <h4>Response Status</h4>
#                                 <h2>{status}</h2>
#                             </div>
#                             """,
#                             unsafe_allow_html=True
#                         )

#                 except Exception as e:

#                     st.error(f"Error occurred: {str(e)}")

import streamlit as st
import requests
import plotly.graph_objects as go
from datetime import datetime
import pandas as pd
import plotly.express as px

# ---------------------------------
# PAGE CONFIG
# ---------------------------------

st.set_page_config(
    page_title="LeadGPT",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=None
)

# ---------------------------------
# CUSTOM CSS
# ---------------------------------

st.markdown("""
    <style>
        /* Main Background */
        .main {
            background-color: #0f1419;
        }
        
        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: #0f1419;
            border-right: 1px solid #1e293b;
        }
        
        /* Headers */
        h1, h2, h3 {
            color: #ffffff;
            font-weight: 700;
            letter-spacing: -0.5px;
        }
        
        /* Response Box */
        .response-box {
            background: linear-gradient(135deg, #1e293b 0%, #0f1419 100%);
            border: 1px solid #334155;
            border-radius: 12px;
            padding: 24px;
            margin: 20px 0;
            color: #e2e8f0;
            line-height: 1.8;
            font-size: 15px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
            position: relative;
            overflow: hidden;
        }
        
        .response-box::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, #3b82f6, #8b5cf6, #ec4899);
        }
        
        /* Stats Cards */
        .stat-card {
            background: linear-gradient(135deg, #1e293b 0%, #0f1419 100%);
            border: 1px solid #334155;
            border-radius: 12px;
            padding: 20px;
            margin: 10px 0;
            text-align: center;
        }
        
        .stat-value {
            font-size: 28px;
            font-weight: 700;
            color: #3b82f6;
            margin: 10px 0;
        }
        
        .stat-label {
            font-size: 13px;
            color: #94a3b8;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        /* Buttons */
        .stButton > button {
            background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
            color: white;
            border: none;
            border-radius: 8px;
            padding: 12px 32px;
            font-weight: 600;
            font-size: 15px;
            width: 100%;
            transition: all 0.3s ease;
            box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
        }
        
        .stButton > button:hover {
            background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
            box-shadow: 0 6px 16px rgba(59, 130, 246, 0.4);
            transform: translateY(-2px);
        }
        
        /* Input Fields */
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea,
        .stNumberInput > div > div > input,
        .stSelectbox > div > div > select {
            background-color: #1e293b !important;
            border: 1px solid #334155 !important;
            color: #e2e8f0 !important;
            border-radius: 8px !important;
            padding: 10px !important;
        }
        
        /* Divider */
        hr {
            border-color: #334155;
        }
        
        /* Info/Success/Warning boxes */
        .stInfo, .stSuccess, .stWarning {
            border-radius: 8px !important;
            border-left: 4px solid #3b82f6 !important;
        }
        
        /* Metric */
        [data-testid="metric-container"] {
            background-color: #1e293b;
            border: 1px solid #334155;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------
# SIDEBAR
# ---------------------------------

with st.sidebar:
    st.markdown("### 🚀 LeadGPT")
    st.markdown("**AI Lead Intelligence Platform**")
    st.markdown("---")
    
    page = st.selectbox(
        "Navigation",
        ["🎯 Dashboard", "📊 Forecasting", "💡 AI Insights", "🤖 RAG Chatbot","📈 Conversational Analytics"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("**System Status**")
    st.success("✓ API Connected")
    st.info("v1.0.0")

# ---------------------------------
# DASHBOARD PAGE
# ---------------------------------

if page == "🎯 Dashboard":

    st.title("Lead Intelligence Dashboard")

    # =========================================
    # LOAD LIVE ANALYTICS
    # =========================================

    try:

        total_leads_response = requests.get(
            "http://127.0.0.1:8000/total-leads"
        )

        converted_response = requests.get(
            "http://127.0.0.1:8000/converted-leads"
        )

        top_agents_response = requests.get(
            "http://127.0.0.1:8000/top-agents"
        )

        top_sources_response = requests.get(
            "http://127.0.0.1:8000/top-sources"
        )

        total_leads = total_leads_response.json()

        converted = converted_response.json()

        top_agents = top_agents_response.json()

        top_sources = top_sources_response.json()

        top_agent_name = top_agents[0]["Sales Agent"]

        top_agent_count = top_agents[0]["Lead Count"]

        top_source_name = top_sources[0]["Lead Source"]

        # =========================================
        # LIVE DASHBOARD CARDS
        # =========================================

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.markdown(f"""
                <div class="stat-card">
                    <div class="stat-label">Total Leads</div>
                    <div class="stat-value">
                        {total_leads["Total Leads"]}
                    </div>
                </div>
            """, unsafe_allow_html=True)

        with col2:

            st.markdown(f"""
                <div class="stat-card">
                    <div class="stat-label">Converted Leads</div>
                    <div class="stat-value">
                        {converted["Converted Leads"]}
                    </div>
                </div>
            """, unsafe_allow_html=True)

        with col3:

            st.markdown(f"""
                <div class="stat-card">
                    <div class="stat-label">Top Sales Agent</div>
                    <div class="stat-value" style="font-size:20px;">
                        {top_agent_name}
                    </div>
                    <p style="color:#94a3b8;">
                        {top_agent_count} Leads
                    </p>
                </div>
            """, unsafe_allow_html=True)

        with col4:

            st.markdown(f"""
                <div class="stat-card">
                    <div class="stat-label">Top Lead Source</div>
                    <div class="stat-value" style="font-size:20px;">
                        {top_source_name}
                    </div>
                </div>
            """, unsafe_allow_html=True)

    except Exception as e:

        st.error(f"Dashboard Analytics Error: {str(e)}")

    st.markdown("---")

        # =========================================
    # AI RECOMMENDATION ENGINE
    # =========================================

    st.markdown("---")

    st.subheader("🧠 AI Business Recommendations")

    try:

        recommendation_response = requests.get(
            "http://127.0.0.1:8000/recommendations"
        )

        recommendation_data = recommendation_response.json()

        recommendations = recommendation_data["recommendations"]

        for recommendation in recommendations:

            st.markdown(f"""
                <div style="
                    background-color:#111827;
                    padding:18px;
                    border-radius:12px;
                    margin-bottom:15px;
                    border-left:5px solid #3b82f6;
                    color:#e2e8f0;
                    font-size:15px;
                    line-height:1.8;
                ">
                    {recommendation}
                </div>
            """, unsafe_allow_html=True)

    except Exception as e:

        st.error(
            f"Recommendation Engine Error: {str(e)}"
        )

    st.subheader("Lead Quality Prediction")



     # =========================================
    # PDF REPORT DOWNLOAD
    # =========================================

    st.markdown("---")

    st.subheader("📄 AI Business Report")

    try:

        report_url = (
            "http://127.0.0.1:8000/generate-report"
        )

        st.markdown(f"""
            <a href="{report_url}" target="_blank">
                <button style="
                    background-color:#2563eb;
                    color:white;
                    padding:12px 24px;
                    border:none;
                    border-radius:10px;
                    font-size:16px;
                    cursor:pointer;
                    width:100%;
                ">
                    📥 Download AI Business Report
                </button>
            </a>
        """, unsafe_allow_html=True)

    except Exception as e:

        st.error(
            f"Report Generation Error: {str(e)}"
        )

    # =========================================
    # LOAD DROPDOWN DATA
    # =========================================

    try:
        product_response = requests.get(
            "http://127.0.0.1:8000/product-ids"
        )

        agent_response = requests.get(
            "http://127.0.0.1:8000/sales-agents"
        )

        location_response = requests.get(
            "http://127.0.0.1:8000/locations"
        )

        product_options = product_response.json()

        agent_options = agent_response.json()

        location_options = location_response.json()

    except Exception as e:
        st.error(f"Error loading dropdown data: {str(e)}")
        product_options = []
        agent_options = []
        location_options = []

    # =========================================
    # INPUT SECTION
    # =========================================

    col1, col2 = st.columns(2)

    with col1:

        product_id = st.selectbox(
            "Product ID",
            product_options
        )

        source = st.selectbox(
            "Lead Source",
            ["Referral", "Website", "Call", "Live Chat"]
        )

        mobile = st.text_input(
            "Mobile Number",
            placeholder="Enter mobile number"
        )

        email = st.text_input(
            "Email",
            placeholder="Enter email address"
        )

    with col2:

        sales_agent = st.selectbox(
            "Sales Agent",
            agent_options
        )

        location = st.selectbox(
            "Location",
            location_options
        )

        delivery_mode = st.selectbox(
            "Delivery Mode",
            ["Online", "Offline"]
        )

        has_mobile = st.selectbox(
            "Has Mobile",
            [0, 1]
        )

    # =========================================
    # DATE INPUTS
    # =========================================

    col3, col4, col5 = st.columns(3)

    with col3:

        day = st.number_input(
            "Day",
            min_value=1,
            max_value=31,
            value=1
        )

    with col4:

        month = st.number_input(
            "Month",
            min_value=1,
            max_value=12,
            value=1
        )

    with col5:

        hour = st.number_input(
            "Hour",
            min_value=0,
            max_value=23,
            value=12
        )

    # =========================================
    # PREDICTION BUTTON
    # =========================================

    if st.button(
        "🔍 Predict Lead Quality",
        use_container_width=True
    ):

        payload = {
          "Product_ID": product_id,
          "Source": source,
          "Mobile": mobile,
          "EMAIL": email,
          "Sales_Agent": sales_agent,
          "Location": location,
          "Delivery_Mode": delivery_mode,

          "Created_Day": day,
          "Created_Month": month,
          "Created_Hour": hour,

          "Has_Mobile": has_mobile,

          # =====================================
          # NEW REQUIRED FEATURES
          # =====================================

          "Valid_Email": 1 if "@" in email else 0,

          "Created_Weekday": 1,

          "Is_Weekend": 0
              }
        try:

            response = requests.post(
                "http://127.0.0.1:8000/predict",
                json=payload
            )

            result = response.json()

            prediction = result["prediction"]

            probability = result["probability"]

            col1, col2 = st.columns(2)

            with col1:

                if prediction == "Good Lead":

                    st.success(
                        f"✓ Prediction: {prediction}"
                    )

                else:

                    st.warning(
                        f"⚠ Prediction: {prediction}"
                    )

            with col2:

                st.metric(
                    "Conversion Probability",
                    f"{probability*100:.1f}%"
                )

            # =========================================
            # GAUGE CHART
            # =========================================

            fig = go.Figure(
                go.Indicator(
                    mode="gauge+number",
                    value=probability * 100,
                    title={
                        'text': "Conversion Probability (%)"
                    },
                    gauge={
                        'axis': {
                            'range': [0, 100]
                        },
                        'bar': {
                            'color': "#3b82f6"
                        },
                        'steps': [
                            {
                                'range': [0, 30],
                                'color': "#ef4444"
                            },
                            {
                                'range': [30, 70],
                                'color': "#f97316"
                            },
                            {
                                'range': [70, 100],
                                'color': "#22c55e"
                            }
                        ]
                    }
                )
            )

            fig.update_layout(
                paper_bgcolor="#0f1419",
                font_color="#e2e8f0",
                font_size=14
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        except Exception as e:

            st.error(f"Error: {str(e)}")

# ---------------------------------
# AI INSIGHTS PAGE
# ---------------------------------

if page == "💡 AI Insights":
    st.title("Business Insights Generator")
    st.markdown("Ask a business question and get AI-powered insights from your data")
    
    st.markdown("---")
    
    prompt = st.text_area(
        "Ask Business Question",
        placeholder="e.g., What are the top revenue drivers? Which products are underperforming?",
        height=120
    )

    if st.button("🎯 Generate Insight", use_container_width=True):
        if not prompt.strip():
            st.warning("Please enter a question")
        else:
            with st.spinner("🔄 Analyzing your question..."):
                try:
                    response = requests.post(
                        "http://127.0.0.1:8000/insight",
                        json={"prompt": prompt}
                    )
                    result = response.json()
                    
                    st.markdown(f"""
                        <div class="response-box">
                        {result["insight"]}
                        </div>
                    """, unsafe_allow_html=True)
                
                except Exception as e:
                    st.error(f"Error: {str(e)}")

# ---------------------------------
# FORECASTING PAGE
# ---------------------------------

if page == "📊 Forecasting":
    st.title("Lead Forecasting")
    st.markdown("30-Day Lead Forecast")
    
    st.markdown("---")

    try:
        response = requests.get("http://127.0.0.1:8000/forecast")
        forecast_data = response.json()

        forecast_df = pd.DataFrame(forecast_data)

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=forecast_df["ds"],
                y=forecast_df["yhat"],
                mode="lines+markers",
                name="Forecast",
                line=dict(color="#3b82f6", width=3),
                marker=dict(size=8)
            )
        )

        fig.update_layout(
            title="Future Lead Forecast",
            xaxis_title="Date",
            yaxis_title="Predicted Leads",
            paper_bgcolor="#0f1419",
            plot_bgcolor="#1e293b",
            font_color="#e2e8f0",
            hovermode="x unified",
            margin=dict(l=50, r=50, t=50, b=50)
        )

        st.plotly_chart(fig, use_container_width=True)

        with st.expander("📋 Forecast Data"):
            st.dataframe(
                forecast_df,
                use_container_width=True,
                hide_index=True
            )
    
    except Exception as e:
        st.error(f"Error loading forecast: {str(e)}")

# ---------------------------------
# RAG CHATBOT PAGE
# ---------------------------------

if page == "🤖 RAG Chatbot":

    # ---------------------------------
    # CHAT MEMORY
    # ---------------------------------

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    st.title("LeadGPT Business Assistant")

    st.markdown("Ask questions about your sales, leads, and business data")

    st.markdown("---")

    # ---------------------------------
    # USER INPUT
    # ---------------------------------

    question = st.text_area(
        "Enter your business question",
        placeholder="e.g., Who are the top sales representatives? What's our revenue by region?",
        height=100
    )

    # ---------------------------------
    # ASK AI BUTTON
    # ---------------------------------

    if st.button("🚀 Ask AI", use_container_width=True):

        if not question.strip():

            st.warning("Please enter a question")

        else:

            with st.spinner("🔄 LeadGPT is analyzing business records..."):

                try:

                    # ---------------------------------
                    # API CALL
                    # ---------------------------------

                    response = requests.post(
                        "http://127.0.0.1:8000/rag",
                        json={"question": question}
                    )

                    result = response.json()

                    # ---------------------------------
                    # HANDLE STRING JSON
                    # ---------------------------------

                    if isinstance(result, str):

                        import json
                        result = json.loads(result)

                    # ---------------------------------
                    # EXTRACT RESPONSE DATA
                    # ---------------------------------

                    answer = result.get("answer", "No answer received")

                    docs_found = result.get("documents_found", 0)

                    status = result.get("status", "success")

                    # ---------------------------------
                    # SAVE CHAT HISTORY
                    # ---------------------------------

                    st.session_state.chat_history.append({
                        "question": question,
                        "answer": answer,
                        "docs": docs_found,
                        "status": status,
                        "time": datetime.now().strftime("%H:%M:%S")
                    })

                except Exception as e:

                    st.error(f"Error: {str(e)}")

                    st.info(
                        "Make sure the API server is running on http://127.0.0.1:8000"
                    )

    # ---------------------------------
    # DISPLAY CHAT HISTORY
    # ---------------------------------

    if st.session_state.chat_history:

        st.markdown("## 💬 Conversation")

        for chat in reversed(st.session_state.chat_history):

            # ---------------------------------
            # USER MESSAGE
            # ---------------------------------

            st.markdown(f"""
                <div style="
                    background-color:#2563eb;
                    padding:16px;
                    border-radius:12px;
                    margin-top:20px;
                    color:white;
                    font-size:15px;
                    line-height:1.7;
                ">
                <b>🧑 You</b><br><br>
                {chat["question"]}
                </div>
            """, unsafe_allow_html=True)

            # ---------------------------------
            # AI RESPONSE
            # ---------------------------------

            st.markdown(f"""
                <div class="response-box">
                <b>🤖 LeadGPT</b><br><br>
                {chat["answer"]}
                </div>
            """, unsafe_allow_html=True)

            # ---------------------------------
            # METADATA
            # ---------------------------------

            col1, col2, col3 = st.columns(3)

            with col1:
                st.info(f"📄 Documents Used: {chat['docs']}")

            with col2:
                status_emoji = "✓" if chat["status"] == "success" else "⚠"
                st.success(
                    f"{status_emoji} Status: {chat['status'].title()}"
                )

            with col3:
                st.info(f"⏱ Generated: {chat['time']}")

            st.markdown("---")

    # =========================================
    # VISUAL ANALYTICS SECTION
    # =========================================

    st.markdown("---")

    st.subheader("📊 Business Analytics Dashboard")

    try:

        # =====================================
        # FETCH ANALYTICS DATA
        # =====================================

        status_response = requests.get(
            "http://127.0.0.1:8000/lead-status"
        )

        locations_response = requests.get(
            "http://127.0.0.1:8000/top-locations"
        )

        top_agents_response = requests.get(
            "http://127.0.0.1:8000/top-agents"
        )

        top_sources_response = requests.get(
            "http://127.0.0.1:8000/top-sources"
        )

        status_data = status_response.json()

        locations_data = locations_response.json()

        agents_data = top_agents_response.json()

        sources_data = top_sources_response.json()

        # =====================================
        # CONVERT TO DATAFRAMES
        # =====================================

        status_df = pd.DataFrame(status_data)

        locations_df = pd.DataFrame(locations_data)

        agents_df = pd.DataFrame(agents_data)

        sources_df = pd.DataFrame(sources_data)

        # =====================================
        # TOP SALES AGENTS BAR CHART
        # =====================================

        st.markdown("### 🏆 Top Sales Agents")

        fig_agents = px.bar(
            agents_df,
            x="Sales Agent",
            y="Lead Count",
            text="Lead Count",
            title="Top Performing Sales Agents"
        )

        fig_agents.update_layout(
            paper_bgcolor="#0f1419",
            plot_bgcolor="#0f1419",
            font_color="#e2e8f0"
        )

        st.plotly_chart(
            fig_agents,
            use_container_width=True
        )

        # =====================================
        # LEAD SOURCE PIE CHART
        # =====================================

        col1, col2 = st.columns(2)

        with col1:

            st.markdown("### 📞 Lead Sources")

            fig_sources = px.pie(
                sources_df,
                names="Lead Source",
                values="Count",
                hole=0.4
            )

            fig_sources.update_layout(
                paper_bgcolor="#0f1419",
                font_color="#e2e8f0"
            )

            st.plotly_chart(
                fig_sources,
                use_container_width=True
            )

        # =====================================
        # LEAD STATUS CHART
        # =====================================

        with col2:

            st.markdown("### 📌 Lead Status Distribution")

            fig_status = px.bar(
                status_df,
                x="Status",
                y="Count",
                text="Count"
            )

            fig_status.update_layout(
                paper_bgcolor="#0f1419",
                plot_bgcolor="#0f1419",
                font_color="#e2e8f0",
                xaxis_tickangle=-30
            )

            st.plotly_chart(
                fig_status,
                use_container_width=True
            )

        # =====================================
        # TOP LOCATIONS CHART
        # =====================================

        st.markdown("### 🌍 Top Lead Locations")

        fig_locations = px.bar(
            locations_df,
            x="Location",
            y="Lead Count",
            text="Lead Count"
        )

        fig_locations.update_layout(
            paper_bgcolor="#0f1419",
            plot_bgcolor="#0f1419",
            font_color="#e2e8f0",
            xaxis_tickangle=-20
        )

        st.plotly_chart(
            fig_locations,
            use_container_width=True
        )

    
    except Exception as e:

        st.error(f"Analytics Visualization Error: {str(e)}")

# ---------------------------------
# CONVERSATIONAL ANALYTICS PAGE
# ---------------------------------

if page == "📈 Conversational Analytics":

    st.title("Conversational Business Analytics")

    st.markdown(
        "Ask analytical business questions using natural language."
    )

    st.markdown("---")

    question = st.text_area(
        "Ask Business Analytics Question",
        placeholder="""
Examples:
- Who is the top sales agent?
- What is the top lead source?
- How many converted leads exist?
- Which location generates most leads?
""",
        height=150
    )

    if st.button(
        "📊 Analyze Business Data",
        use_container_width=True
    ):

        if question.strip() == "":

            st.warning(
                "Please enter a business analytics question."
            )

        else:

            with st.spinner(
                "Analyzing business data..."
            ):

                try:

                    response = requests.post(
                        "http://127.0.0.1:8000/analytics-chat",
                        json={
                            "question": question
                        }
                    )

                    result = response.json()

                    answer = result["answer"]

                    st.markdown("## 📈 Analytics Result")

                    st.markdown(
    f"""
    <div style="
        background-color:#111827;
        padding:20px;
        border-radius:12px;
        border-left:5px solid #3b82f6;
        color:#e2e8f0;
        line-height:1.8;
        font-size:15px;
    ">
        {answer}
    </div>
    """,
    unsafe_allow_html=True
)

                except Exception as e:

                    st.error(
                        f"Conversational Analytics Error: {str(e)}"
                    )