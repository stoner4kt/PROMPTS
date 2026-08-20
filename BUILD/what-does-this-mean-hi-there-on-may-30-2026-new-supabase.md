# What does this mean (Hi there, On May 30, 2026, new Supabase

What does this mean (Hi there,

On May 30, 2026, new Supabase projects won't expose tables in the "public" schema to the Data API by default. Any new table you create in "public" will require an explicit GRANT before it can be accessed through PostgREST, GraphQL, or supabase-js.

 

Existing projects keep the current default behavior until October 30, 2026.

 

What to do

 

Add explicit grants to your table-creation flow. The changelog post has the full SQL and migration guidance.

Read the changelog post

Rollout dates

 

May 30, 2026: Default for all new projects
October 30, 2026: Enforced on new tables across all existing projects

Ahead of October 30, use the Security Advisor in your dashboard to review which tables are currently exposed to the Data API.

)
