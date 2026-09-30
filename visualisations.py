import plotly.express as px
import pandas as pd
def risk_time(data):
    graph1 = px.line(data,
                x = "timestamp",
                y = "risk_score",
                title = "Risk over Time"
                     )
    graph1.update_traces(line=dict(color="#0F766E"))
    return graph1

def sleep_vs_risk(data):
    graph2 = px.line(data,
                        x = "sleep_hours",
                        y = "risk_score",
                     title="Sleep Hours Vs. Risk Score",
                     markers = True
                        )
    graph2.update_traces(line=dict(color="#8B5CF6"))
    return graph2

def stress_vs_risk(data):
    graph3 = px.line(data,
                        x = "stress",
                        y = "risk_score",
                     title="Stress Level Vs. Risk Score",
                     markers = True
                        )
    graph3.update_traces(line=dict(color="#D97706"))
    return graph3

