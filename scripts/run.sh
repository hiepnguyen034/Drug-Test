#curl -LO https://github.com/tensorflow/tensorflow/raw/master/tensorflow/examples/label_image/label_image.py
python label_image.py \
--graph=output_graph.pb --labels=output_labels.txt \
--input_layer=Placeholder \
--output_layer=final_result \
--image=eyes_photos/normal/hiep_test.jpg


