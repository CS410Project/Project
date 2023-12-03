# Project
Project Proposal: [PDF](https://github.com/CS410Project/Project/blob/main/project_proposal.pdf)

# Project Progress Report
Project Progress Report: https://github.com/CS410Project/Project/blob/main/Project%20Progress%20Report.pdf

# Install and Run
## Installation
1. Clone the repo and enter project root directory
2. In terminal, type `make install` to install all dependencies

## Debug
1. In terminal, type `make debug` and keep it running
2. Open browser and go to `http://127.0.0.1:5000/`
3. For other usages, check `app/view.py` for more examples

## Run
1. In terminal, type `make run` and keep it running, the data will be processed every 60s
2. Open browser and go to `http://127.0.0.1:5000/`
3. For top-10 hitters, go to `http://127.0.0.1:5000/top_k_hitters` (might delay a few seconds due to browser cache)
4. For detailed video analysis, go to `http://127.0.0.1:5000/video_cache`
5. For other usages, check `app/view.py` for more examples
6. When finished, type `make stop` to stop the server

## Log
1. Logs are stored in `logs/` directory
2. `access.log` is the general Flask access log
3. `error.log` is the general Flask networking/setup/traffic log
4. `unified_worker.log` is the log for the unified worker python script

# Team Contribution 
a.	Data feed
    i.	Shuxian Xu - sx30
    ii.	You Zhou - youzhou3
b.	Data parsing
    i.	Tianyu Zhou - aliang7
    ii.	You Zhou - youzhou3
c.	Platform construction
    i.	Tianyi Zhang - tianyi18
    ii.	Tianyu Zhou - aliang7
d.	Map-reduce 
    i.	Shuxian Xu - sx30
    ii.	Tianyi Zhang - tianyi18
    iii. Tianyu Zhou - aliang7
    iv.	You Zhou - youzhou3
e.	Result rendering
    i.	Tianyi Zhang - tianyi18
    ii.	Shuxian Xu - sx30
f.	Documentation
    i.	Shuxian Xu - sx30
    ii.	Tianyi Zhang - tianyi18
    iii. Tianyu Zhou - aliang7
    iv.	You Zhou - youzhou3
g.	Code Review
    i.	Tianyi Zhang - tianyi18
h.	Final Presentation 
    i.	Shuxian Xu - sx30
    ii.	Tianyi Zhang - tianyi18
    iii. Tianyu Zhou - aliang7
    iv.	You Zhou - youzhou3

