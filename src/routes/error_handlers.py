from flask import Blueprint

from flask import current_app, render_template
errors = Blueprint('errors',__name__)

@errors.app_errorhandler(404)
def not_found(e):
    return render_template('error.html',error_code=404,error_message="page not found"),404
@errors.app_errorhandler(500)
def server_error(e):
    return render_template('error.html',error_code=500,error_message="server error"),500
@errors.app_errorhandler(403)
def forbidden(e):
    return render_template('error.html',error_code=403,error_message="forbidden"),403
@errors.app_errorhandler(401)
def unauthorized(e):
    return render_template('error.html',error_code=401,error_message="unauthorized"),401
@errors.app_errorhandler(400)
def bad_request(e):
    return render_template('error.html',error_code=400,error_message="bad request"),400
@errors.app_errorhandler(405)
def method_not_allowed(e):
    return render_template('error.html',error_code=405,error_message="method not allowed"),405
@errors.app_errorhandler(503)
def service_unavailable(e):
    return render_template('error.html',error_code=503,error_message="service unavailable"),503
@errors.app_errorhandler(408)
def request_timeout(e):
    return render_template('error.html',error_code=408,error_message="request timeout"),408
@errors.app_errorhandler(409)
def conflict(e):
    return render_template('error.html',error_code=409,error_message="conflict"),409
@errors.app_errorhandler(410)
def gone(e):
    return render_template('error.html',error_code=410,error_message="gone"),410
@errors.app_errorhandler(411)
def length_required(e):
    return render_template('error.html',error_code=411,error_message="length required"),411
@errors.app_errorhandler(412)
def precondition_failed(e):
    return render_template('error.html',error_code=412,error_message="precondition failed"),412
@errors.app_errorhandler(413)
def request_entity_too_large(e):
    return render_template('error.html',error_code=413,error_message="request entity too large"),413
@errors.app_errorhandler(414)
def request_uri_too_large(e):
    return render_template('error.html',error_code=414,error_message="request uri too large"),414
@errors.app_errorhandler(415)
def unsupported_media_type(e):
    return render_template('error.html',error_code=415,error_message="unsupported media type"),415
@errors.app_errorhandler(416)
def requested_range_not_satisfiable(e):
    return render_template('error.html',error_code=416,error_message="requested range not satisfiable"),416
@errors.app_errorhandler(417)
def expectation_failed(e):
    return render_template('error.html',error_code=417,error_message="expectation failed"),417
@errors.app_errorhandler(418)
def teapot(e):
    return render_template('error.html',error_code=418,error_message="teapot"),418
@errors.app_errorhandler(422)
def unprocessable_entity(e):
    return render_template('error.html',error_code=422,error_message="unprocessable entity"),422
@errors.app_errorhandler(423)
def locked(e):
    return render_template('error.html',error_code=423,error_message="locked"),423
@errors.app_errorhandler(424)
def failed_dependency(e):
    return render_template('error.html',error_code=424,error_message="failed dependency"),424

@errors.app_errorhandler(428)
def precondition_required(e):
    return render_template('error.html',error_code=428,error_message="precondition required"),428
@errors.app_errorhandler(429)
def too_many_requests(e):
    return render_template('error.html',error_code=429,error_message="too many requests"),429
