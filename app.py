{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4ac538c5",
   "metadata": {},
   "outputs": [],
   "source": [
    "#caps sentitive\n",
    "from flask import Flask"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "0abc1758",
   "metadata": {},
   "outputs": [],
   "source": [
    "#app style declarator is __\n",
    "app=Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "694bd130",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import request, render_template\n",
    "import joblib\n",
    "\n",
    "#Get results and Post answers, add float to make sure users can only type in INT\n",
    "@app.route(\"/\",methods=[\"GET\",\"POST\"])\n",
    "def index ():\n",
    "    if request.method ==\"POST\":\n",
    "        rates=request.form.get(\"rates\")\n",
    "        print(rates)\n",
    "        model=joblib.load(\"DBS\")\n",
    "        pred=model.predict([[float(rates)]])\n",
    "        print(pred)\n",
    "        s=\"The predicted DBS share price is \" +str(pred[0][0])\n",
    "        return(render_template(\"index.html\", result= s))\n",
    "    else:\n",
    "        return(render_template(\"index.html\", result=\"2\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "47ae494d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n",
      "127.0.0.1 - - [12/Feb/2022 16:36:31] \"GET / HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [12/Feb/2022 16:36:34] \"POST / HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[24.44735922]]\n"
     ]
    }
   ],
   "source": [
    "#to authentical if this program is yours\n",
    "if __name__==\"__main__\":\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bdeca948",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
