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
1. Architecture Design: Tianyi Zhang - tianyi18
2. Data feed: Shuxian Xu - sx30; You Zhou - youzhou3
3. Data parsing: Tianyu Zhou - aliang7; You Zhou - youzhou3
4. Platform construction: Tianyi Zhang - tianyi18; Tianyu Zhou - aliang7
5. Map-reduce: Shuxian Xu - sx30; Tianyi Zhang - tianyi18; Tianyu Zhou - aliang7; You Zhou - youzhou3
6. Result rendering: Tianyi Zhang - tianyi18; Shuxian Xu - sx30
7. Documentation: Shuxian Xu - sx30; Tianyi Zhang - tianyi18; Tianyu Zhou - aliang7; You Zhou - youzhou3
8. Code Review: Tianyi Zhang - tianyi18
9. Final Presentation: Shuxian Xu - sx30; Tianyi Zhang - tianyi18; Tianyu Zhou - aliang7; You Zhou - youzhou3

