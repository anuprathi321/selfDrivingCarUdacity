#!/usr/bin/env python3

import tensorflow as tf

x = tf.placeholder(tf.int32)

with tf.Session() as sess:
	output = sess.run(x, feed_dict={x:42})
	print(output)
