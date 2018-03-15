# Revision History

## 0.3 (2018/03/15)

- Exposed `logging` level constants on the `log` package.
- Added `log.WARN` as an alias of `log.WARNING`.

## 0.2.1 (2018/03/04)

- Removed the Python version check on installation.

## 0.2 (2018/03/03)

- Added method to force logging format: `log.init(format="...")`
- Added method to silenced named loggers: `log.silence('requests', allow_error=True)`
- Added convenience aliases: `log.d`, `log.i`, `log.w`, `log.e`

## 0.1 (2018/03/03)

 - Initial release.
