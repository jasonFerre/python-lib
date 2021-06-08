class FakeContext:
    function_name = "FUNCTION_NAME"
    memory_limit_in_mb = 1024
    invoked_function_arn = "INVOKED_FUNCTION_ARN"
    aws_request_id = "AWS_REQUEST_ID"
    log_group_name = "LOG_GROUP_NAME"
    log_stream_name = "LOG_STREAM_NAME"

    def get_remaining_time_in_millis(self):
        # 5 minutes
        return 300000
