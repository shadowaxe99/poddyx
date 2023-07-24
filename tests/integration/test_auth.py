# tests/integration/test_auth.py

import requests
import pytest

BASE_URL = 'http://localhost:5000'

def test_user_signup():

  # Test invalid email 
  data = {'email': 'invalid', 'password': 'pass123'}
  response = requests.post(f"{BASE_URL}/signup", json=data)
  assert response.status_code == 400

  # Test short password
  data = {'email': 'validemail@test.com', 'password': 'short'}
  response = requests.post(f"{BASE_URL}/signup", json=data)
  assert response.status_code == 400

  # Valid signup
  data = {'email': 'validemail@test.com', 'password': 'goodpassword'}
  response = requests.post(f"{BASE_URL}/signup", json=data)
  assert response.status_code == 201
  
  # Verify user was created
  response = requests.get(f"{BASE_URL}/users")
  users = response.json()
  assert any(u['email'] == 'validemail@test.com' for u in users)