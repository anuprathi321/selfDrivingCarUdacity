#!/usr/bin/env python3

import tensorflow as tf

hello_constant = tf.constant("hello world")

with tf.Session() as sess:
	output = sess.run(hello_constant)
	print(output)
	
#sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
