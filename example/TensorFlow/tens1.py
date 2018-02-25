import tensorflow as tf
x = tf.placeholder(tf.float32,name='x')
y = tf.placeholder(tf.float32,name='y')
z = tf.add(x, y,name='sum')

with tf.Session() as sess:  
    init=tf.gloabal_variables_initializer()
    sess.run(init)
    print(sess.run(z,feed_dict={x:5.5,y:2.1}))
  
tf.summary.merge_all()
filewriter=tf.summary.FileWriter(log/sum,sess.graph)