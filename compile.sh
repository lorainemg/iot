# Helper bash script to compile protobuf files
# Example of usage: ./compile.sh "mqtt_client/protos"  "downlink.proto"

# Dir were the proto file and the python file will be located
DIR=$1
# Filename of the protobuff file
PROTONAME=$2

echo $DIR
protoc -I=$DIR --python_out=$DIR $DIR/$PROTONAME