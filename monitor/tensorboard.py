import mxnet as mx
from mxnet.tensorboard import TensorBoardMonitor, histogram, scalar
from utils.args import get, check
from utils.parse_args import str2list


def get_monitor(**kwargs):
    from utils.logger import get_logger
    pattern = get(kwargs, 'pattern', str2list, None)
    interval = get(kwargs, 'interval', int, 100)
    prefix = get(kwargs, 'prefix', str, kwargs['console_arg'].symbol_name + '.')
    check(kwargs, 'monitor.tensorboard', ['pattern', 'interval', 'prefix'])

    monitor = TensorBoardMonitor(
        pattern_callback_map={key: [scalar, histogram]for key in pattern},
        reject_pattern='.*label',
        interval=interval, profile_logging=True, logger=get_logger(),
        symbol_name_prefix=prefix)  # tensorboard monitor per 1k batch
    return monitor