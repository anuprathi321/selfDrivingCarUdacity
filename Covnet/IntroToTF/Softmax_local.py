#!/usr/bin/env python3

import numpy as np
import tensorflow as tf

logit_data = [0.0001, 0.000, 0.0003]

logits = tf.placeholder(tf.float32)

with tf.Session() as sess:
	softmax=tf.nn.softmax(logits)
	output=sess.run(softmax, feed_dict={logits:logit_data})

print(output)
