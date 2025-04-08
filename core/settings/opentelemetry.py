# from opentelemetry import trace
# from opentelemetry.propagate import set_global_textmap
# from opentelemetry.sdk.trace import TracerProvider
# from sentry_sdk.integrations.opentelemetry import SentrySpanProcessor, SentryPropagator

# provider = TracerProvider()
# provider.add_span_processor(SentrySpanProcessor())
# trace.set_tracer_provider(provider)
# set_global_textmap(SentryPropagator())