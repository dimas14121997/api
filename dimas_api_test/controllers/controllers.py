from crypt import methods
from enum import auto
import json
import requests
from odoo.tests import Form
import werkzeug.wrappers

from odoo import http, _ , exceptions
from odoo.http import request

class SearchKampus(http.Controller):
    @http.route(['/dimas_api_test1/search_kampus/'], type='http',website=False, auth="public", methods=['GET'], csrf=False)
    def search_kampus(self,**params):
        test_api = request.env['dimas.kampus'].sudo().search([])
        dict_test = {}
        data_test_api = []
        for h in test_api:
            dict_test = {
                'id':h.id,
                'name':h.name,
                'jenis_kampus':h.jenis_kampus,
                'Akreditasi':h.akreditasi,
                'status':h.status,
                'no_telp':h.no_telp,
                'fax':h.fax,
                'alamat':h.alamat,
                }
            data_test_api.append(dict_test)
        data = {
            'status':200,
            'message':'success',
            'response':data_test_api
        }
        try:
            return werkzeug.wrappers.Response(
                status=200,
                content_type='application/json; charset=utf-8',
                response=json.dumps(data)
            )
        except:
            return werkzeug.wrappers.Response(
                status=400,
                content_type='application/json; charset=utf-8',
                headers=[('Access-Control-Allow-Origin','*')],
                response=json.dumps({
                    'error':'Error',
                    'error_descrip':'Error Description'
                })
            )

    @http.route(['/dimas_api_test1/search_kampus_by_name/'], type='http',website=False, auth="public", methods=['GET'], csrf=False)
    def search_kampus_by_name(self,**params):
        get_name = params.get('name')
        test_api = request.env['dimas.kampus'].sudo().search([('name','like',get_name)])

        dict_test = {}
        data_test_api = []
        for h in test_api:
            dict_test = {
                'id':h.id,
                'name':h.name,
                'jenis_kampus':h.jenis_kampus,
                'Akreditasi':h.akreditasi,
                'status':h.status,
                'no_telp':h.no_telp,
                'fax':h.fax,
                'alamat':h.alamat,
                }
            data_test_api.append(dict_test)
        data = {
            'status':200,
            'message':'success',
            'response':data_test_api
        }
        try:
            return werkzeug.wrappers.Response(
                status=200,
                content_type='application/json; charset=utf-8',
                response=json.dumps(data)
            )
        except:
            return werkzeug.wrappers.Response(
                status=400,
                content_type='application/json; charset=utf-8',
                headers=[('Access-Control-Allow-Origin','*')],
                response=json.dumps({
                    'error':'Error',
                    'error_descrip':'Error Description'
                })
            )
    @http.route(['/dimas_api_test1/list_jurusan/'], type='http',website=False, auth="public", methods=['GET'], csrf=False)
    def list_jurusan(self,**params):
        test_api = request.env['dimas.kampus'].sudo().search([])
        # get_id = params.get('oi')
        # test_api = request.env['dimas.sale'].sudo().search([('id','=',get_id)])
        
        dict_test = {}
        data_test_api = []
        for h in test_api:
            jurusan_dict = {}
            jurusan_list = []
            get_jurusan = request.env['dimas.jurusan'].sudo().search([('name_kampus_ids','=',h.id)])

            for b in get_jurusan:
                jurusan_dict = {
                   'name':b.name, 
                   'akreditasi':b.akreditasi, 
                }
                jurusan_list.append(jurusan_dict)
           
            dict_test = {
                'name':h.name,
                'jurusan':jurusan_list

                }
            data_test_api.append(dict_test)
        data = {
            'status':200,
            'message':'success',
            'response':data_test_api
        }
        try:
            return werkzeug.wrappers.Response(
                status=200,
                content_type='application/json; charset=utf-8',
                response=json.dumps(data)
            )
        except:
            return werkzeug.wrappers.Response(
                status=400,
                content_type='application/json; charset=utf-8',
                headers=[('Access-Control-Allow-Origin','*')],
                response=json.dumps({
                    'error':'Error',
                    'error_descrip':'Error Description'
                })
            )
    
    @http.route(['/dimas_api_test1/list_jurusan_by_name/'], type='http',website=False, auth="public", methods=['GET'], csrf=False)
    def list_jurusan_by_name(self,**params):
        
        get_name = params.get('name')
        test_api = request.env['dimas.kampus'].sudo().search([('name','like',get_name)])
        print(test_api)
        dict_test = {}
        data_test_api = []
        for h in test_api:
            jurusan_dict = {}
            jurusan_list = []
            get_jurusan = request.env['dimas.jurusan'].sudo().search([('name_kampus_ids','=',h.id)])

            for b in get_jurusan:
                jurusan_dict = {
                   'name':b.name, 
                   'akreditasi':b.akreditasi, 
                }
                jurusan_list.append(jurusan_dict)
          
            dict_test = {
                'name':h.name,
                'jurusan':jurusan_list

                }
            data_test_api.append(dict_test)
        data = {
            'status':200,
            'message':'success',
            'response':data_test_api
        }
        try:
            return werkzeug.wrappers.Response(
                status=200,
                content_type='application/json; charset=utf-8',
                response=json.dumps(data)
            )
        except:
            return werkzeug.wrappers.Response(
                status=400,
                content_type='application/json; charset=utf-8',
                headers=[('Access-Control-Allow-Origin','*')],
                response=json.dumps({
                    'error':'Error',
                    'error_descrip':'Error Description'
                })
            )
    
    @http.route(['/dimas_api_test1/add_follow_kampus/'], type='json', auth="public", methods=['POST'], csrf=False)
    def add_follow_kampus(self,**params):
        order = params.get('order')
        name = order[0]['name']
        name_kampus_ids = order[0]['name_kampus_ids']
   
        names_obj = request.env['res.users'].sudo().search([('name','like',name)])    
        name_kampus_obj = request.env['dimas.kampus'].sudo().search([('name','like',name_kampus_ids)])  
        
        vals_header = {
            'name':names_obj.id,
            'name_kampus_ids':name_kampus_obj.id
        }
        print('vals_header=>>',vals_header)
        new_add = request.env['dimas.follow.kampus'].sudo().create(vals_header)
        data = {
            'status':200,
            'message':'success',
            'name':name,
            'name_kampus_ids':name_kampus_ids
        }

        return data