# import sentry_sdk

# sentry_sdk.init(
#     dsn="https://d2f579e6ffa0fb2d2b36a281c9cfbcfb@o4507295074353152.ingest.de.sentry.io/4507334919454800",
#     # Set traces_sample_rate to 1.0 to capture 100%
#     # of transactions for performance monitoring.
#     traces_sample_rate=1.0,
#     # Set profiles_sample_rate to 1.0 to profile 100%
#     # of sampled transactions.
#     # We recommend adjusting this value in production.
#     profiles_sample_rate=1.0,
#     enable_tracing=True,
#     # set the instrumenter to use OpenTelemetry instead of Sentry
#     instrumenter="otel",
# )