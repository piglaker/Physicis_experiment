call activate pythontf
python record_and_solve.py
python img2video.py
python predict.py
cd pytorch-ssd-master
python run_ssd_examples_batch.py mb1-ssd models/mb1-ssd-car.pth models/open-images-model-labels.txt 0.jpg
cd ..
python add_frame.py
cd AlphaPose
python video_demo.py --video ../static/img/video2.mp4 --outdir ../static/img/alphapose-video2 --save_video --sp --vis_fast
cd ..
python score.py
python ok.py
python connect.py

