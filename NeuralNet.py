# import tensorflow as tf
# from tensorflow.examples.tutorials.mnist import input_data
# import ReadAndCreateDic as reader
# import FindMode 
# import pickle
# from sklearn import preprocessing, cross_validation, svm
# import numpy as np
# 
# data = reader.getData()
# #modePrimaryCause, modeCrashType = FindMode.findMode('Sunday', 35.19705901, -80.93564375, 20, data)
# 
# 
# dicPrimaryCause, dicCrashType, dicDayValues = reader.createDictionary()
# save_dicPrimaryCause = open("dicPrimaryCause.pickle","wb")
# pickle.dump(dicPrimaryCause, save_dicPrimaryCause)
# save_dicPrimaryCause.close()
#     
# save_dicCrashType = open("dicCrashType.pickle","wb")
# pickle.dump(dicCrashType, save_dicCrashType)
# save_dicCrashType.close()
#    
# save_dicDayValues = open("dicDayValues.pickle", "wb")
# pickle.dump(dicDayValues, save_dicDayValues)
# save_dicDayValues.close()
# 
# # open_dicPrimaryCause = open("dicPrimaryCause.pickle", "rb")
# # dicPrimaryCause = pickle.load(open_dicPrimaryCause)
# # open_dicPrimaryCause.close()
# #    
# # open_dicCrashType = open("dicCrashType.pickle", "rb")
# # dicCrashType = pickle.load(open_dicCrashType)
# # open_dicCrashType.close()
#   
# #open_dicDayValues = open("dicDayValues.pickle", "rb")
# #dicDayValues = pickle.load(open_DicDayValues)
# #open_dicDayValues.close()
# 
#  
# #print(dicPrimaryCause[modePrimaryCause], dicCrashType[modeCrashType])
# # print(data.head())
# #  
# # X = np.array(data[['MILT_TIME', 'LATITUDE', 'LONGITUDE']].as_matrix())
# # y = np.array(data['PRIMARY_CAUSE_CD'].as_matrix())
# #  
# # train_x =X
# # train_y =y
# # test_x =X
# # test_y =y
# #    
# # n_nodes_hl1 = 500 
# # n_nodes_hl2 = 500 
# # n_nodes_hl3 = 500
# #      
# # n_classes = 1
# # batch_size = 100
# # input_size = 3 
# # hm_epochs= 1
# # 
# # x = tf.placeholder('float',[None, input_size])
# # y = tf.placeholder('float')
# # 
# # hidden_1_layer = {'f_fum':n_nodes_hl1,
# #                   'weight':tf.Variable(tf.random_normal([input_size, n_nodes_hl1])),
# #                   'bias':tf.Variable(tf.random_normal([n_nodes_hl1]))}
# # 
# # hidden_2_layer = {'f_fum':n_nodes_hl2,
# #                   'weight':tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])),
# #                   'bias':tf.Variable(tf.random_normal([n_nodes_hl2]))}
# # 
# # hidden_3_layer = {'f_fum':n_nodes_hl3,
# #                   'weight':tf.Variable(tf.random_normal([n_nodes_hl2, n_nodes_hl3])),
# #                   'bias':tf.Variable(tf.random_normal([n_nodes_hl3]))}
# # 
# # output_layer = {'f_fum':None,
# #                 'weight':tf.Variable(tf.random_normal([n_nodes_hl3, n_classes])),
# #                 'bias':tf.Variable(tf.random_normal([n_classes])),}
# # 
# # 
# # # Nothing changes
# # def neural_network_model(data):
# # 
# #     l1 = tf.add(tf.matmul(data,hidden_1_layer['weight']), hidden_1_layer['bias'])
# #     l1 = tf.nn.relu(l1)
# # 
# #     l2 = tf.add(tf.matmul(l1,hidden_2_layer['weight']), hidden_2_layer['bias'])
# #     l2 = tf.nn.relu(l2)
# # 
# #     l3 = tf.add(tf.matmul(l2,hidden_3_layer['weight']), hidden_3_layer['bias'])
# #     l3 = tf.nn.relu(l3)
# # 
# #     output = tf.matmul(l3,output_layer['weight']) + output_layer['bias']
# # 
# #     return output
# # 
# # saver = tf.train.Saver()
# # 
# # def train_neural_network(x):
# #     prediction = neural_network_model(x)
# #     cost = tf.reduce_mean(tf.abs(tf.subtract(prediction,y)))
# #     optimizer = tf.train.AdamOptimizer(learning_rate=0.001).minimize(cost)
# # 
# #     with tf.Session() as sess:
# #         sess.run(tf.global_variables_initializer())
# #         
# #         for epoch in range(hm_epochs):
# #             epoch_loss = 0
# #             i=0
# #             while i < len(train_x):
# #                 start = i
# #                 end = i+batch_size
# #                 batch_x = train_x[start:end]
# #                 batch_y = train_y[start:end]
# # 
# # 
# #                 _, c = sess.run([optimizer, cost], feed_dict={x: batch_x,
# #                                                               y: batch_y})
# #                 epoch_loss += c
# #                 i+=batch_size
# #                 
# #             saver.save(sess, "./trained_variables.ckpt")
# #             print('Epoch', epoch+1, 'completed out of',hm_epochs,'loss:',epoch_loss)
# # #         correct = tf.equal(tf.argmax(prediction), tf.argmax(y))
# # #         accuracy = tf.reduce_mean(tf.cast(correct, 'float'))
# #  
# # #         print('Accuracy:',accuracy.eval({x:test_x, y:test_y}))
# # 
# # def use_neural_network(input_data):
# #     prediction = neural_network_model(x)
# # 
# #     with tf.Session() as sess:
# #         sess.run(tf.initialize_all_variables())
# #         saver.restore(sess, "./trained_variables.ckpt")
# # 
# #         # pos: [1,0] , argmax: 0
# #         # neg: [0,1] , argmax: 1
# #         result = (sess.run(prediction.eval(feed_dict={x:[input_data]}),1))
# #     return result
# #             
# # train_neural_network(x)
# # with tf.Session() as sess:
# #     x = use_neural_network([0.000,35.19705901, -80.93564375])
# #     gdf= neural_network_model(x)
# #     1+1