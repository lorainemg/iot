.PHONY: compile

SRC_DIR := protos
DST_DIR := protos


compile:
	protoc -I=$(SRC_DIR) --python_out=$(DST_DIR) $(SRC_DIR)/downlink.proto