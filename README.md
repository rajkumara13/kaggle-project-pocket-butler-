# PocketButler — Personal Concierge Agent
# Pocket Butler 🧑‍🍳🛒 – Personal Concierge Agent

## Overview
Pocket Butler is an AI-powered personal concierge agent designed to simplify everyday tasks such as meal planning, grocery shopping, pantry management, and daily task organization. It acts as a **virtual assistant**, helping users save time, reduce stress, and streamline their routines.

---

## Problem
Daily life involves repetitive tasks that consume time and mental energy:

- Planning meals every week  
- Creating grocery lists based on available pantry items  
- Tracking pantry inventory  
- Managing daily reminders and tasks  

These small tasks are often overlooked but add up, taking hours every week.

---

## Solution
Pocket Butler automates these tasks using AI agents:

- **Meal Planner Agent:** Suggests weekly meal plans based on preferences and available ingredients.  
- **Grocery Agent:** Generates shopping lists automatically from planned meals.  
- **Pantry Agent:** Tracks what items are available and what needs replenishing.  
- **Task/Reminder Agent:** Helps manage daily tasks, reminders, and schedules.  

By combining multiple agents, Pocket Butler provides an intelligent, personalized assistant experience.

---

## Features
- Multi-agent system (Meal Planner, Grocery, Pantry, Task Agent)  
- Persistent memory for user preferences and pantry inventory  
- Custom tools for recipe searching and pantry management  
- Optional integration with Google Search API for dynamic recipe suggestions  
- Simple command-line interface for interaction  
- Modular architecture for easy future expansion  

---

## Architecture
 ┌──────────────────────────────────────────────────────────────────┐
 │                        POCKET BUTLER SYSTEM                      │
 └──────────────────────────────────────────────────────────────────┘

                   ┌───────────────────────────┐
                   │   User Input / Interface   │
                   └──────────────┬────────────┘
                                  │
                        Natural Language Query
                                  │
                ┌────────────────▼────────────────┐
                │     Orchestrator / Manager      │
                │        (Main Agent)             │
                └────────────────┬────────────────┘
                                │ Intent Routing
     ┌──────────────────────────┼──────────────────────────────┐
     │                          │                              │
┌────▼─────┐            ┌───────▼──────────┐          ┌────────▼─────────┐
│ Task     │            │ Smart Search     │          │ Reminder Agent     │
│ Planner  │            │ Agent            │          │ (Memory + Tool)    │
│ Agent    │            └───────┬──────────┘          └───────┬───────────┘
└────┬─────┘                    │                             │
     │                           │ Search Query                │ Save / Fetch Reminders
     │                           │                             │
     │                  ┌────────▼──────────┐           ┌──────▼───────────┐
     │                  │ Google Search API │           │ Reminder Tool DB  │
     │                  └───────────────────┘           └───────────────────┘
     │
     │  Creates plans
     │
┌────▼──────────┐     ┌─────────────────────────┐      ┌──────────────────────────┐
│ Meal / Routine │     │ Shopping Comparison     │      │ Summarizer / Writing     │
│ Planner Agent  │     │ Agent                   │      │ Agent                    │
└─────┬──────────┘     └───────────┬────────────┘      └──────────┬──────────────┘
      │                            │ Price Lookup                    │ Summaries / Notes
      │                            │                                 │
      │                     ┌────────▼───────────┐            ┌──────▼─────────────┐
      │                     │ Product Price API  │            │ Code Execution Tool │
      │                     └────────────────────┘            └─────────────────────┘
      │
      │
┌─────▼────────────┐
│ Memory Bank      │  <-- stores user prefs, history, routines
└──────────────────┘

##Create virtual environment and install dependencies
python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows
pip install -r requirements.txt

##FINALY RUN THIS 
python -m backend.main
