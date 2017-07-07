# generate_tfrecord
    Generate_tfrecord allows you to make tensorflow tfrecord with your own images.
    To use the code to generate the tf_record,first put the picture by classnames in the root.
    You can config the root in settings.py.
    And config all the settings in settings.py.(Usually, you only need to change the matching_name,root and the pre_process code)
    And run generate_tfrecords.py or generate_tfrecords_with_shuffle.py then you finish!
    If you choose with_shuffle,your tfrecord data will be shuffled and you will easily use it if you use it in a batch train.
    If not,your tfrecord data will not be shuffled.If you want to shuffle it during the train phase,you should use the tf.train.shuffle_batch to shuffle when using Tensorflow to train your network.I suggest you use generate_tfrecords_with_shuffle.py
    to shuffle during the making tfrecord phase.
