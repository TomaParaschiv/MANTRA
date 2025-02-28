PGDMP                      }            postgres    17.2    17.1                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false                        0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            !           1262    5    postgres    DATABASE     �   CREATE DATABASE postgres WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
    DROP DATABASE postgres;
                     postgres    false            "           0    0    DATABASE postgres    COMMENT     N   COMMENT ON DATABASE postgres IS 'default administrative connection database';
                        postgres    false    4897                        2615    16480    public    SCHEMA     2   -- *not* creating schema, since initdb creates it
 2   -- *not* dropping schema, since initdb creates it
                     postgres    false            #           0    0    SCHEMA public    COMMENT         COMMENT ON SCHEMA public IS '';
                        postgres    false    5            $           0    0    SCHEMA public    ACL     +   REVOKE USAGE ON SCHEMA public FROM PUBLIC;
                        postgres    false    5            �            1259    16474    food    TABLE       CREATE TABLE public.food (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    kcal numeric(10,2) NOT NULL,
    carbs numeric(10,2) NOT NULL,
    protein numeric(10,2) NOT NULL,
    fats numeric(10,2) NOT NULL,
    category character varying(50) NOT NULL
);
    DROP TABLE public.food;
       public         heap r       postgres    false    5            �            1259    16473    food_id_seq    SEQUENCE     �   CREATE SEQUENCE public.food_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 "   DROP SEQUENCE public.food_id_seq;
       public               postgres    false    5    218            %           0    0    food_id_seq    SEQUENCE OWNED BY     ;   ALTER SEQUENCE public.food_id_seq OWNED BY public.food.id;
          public               postgres    false    217            �           2604    16477    food id    DEFAULT     b   ALTER TABLE ONLY public.food ALTER COLUMN id SET DEFAULT nextval('public.food_id_seq'::regclass);
 6   ALTER TABLE public.food ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    217    218    218                      0    16474    food 
   TABLE DATA           N   COPY public.food (id, name, kcal, carbs, protein, fats, category) FROM stdin;
    public               postgres    false    218   0       &           0    0    food_id_seq    SEQUENCE SET     9   SELECT pg_catalog.setval('public.food_id_seq', 1, true);
          public               postgres    false    217            �           2606    16479    food food_pkey 
   CONSTRAINT     L   ALTER TABLE ONLY public.food
    ADD CONSTRAINT food_pkey PRIMARY KEY (id);
 8   ALTER TABLE ONLY public.food DROP CONSTRAINT food_pkey;
       public                 postgres    false    218                 x���Ks�0�ח_�M��X��Ф]$��t2�t�a4��E���^�/R�v���tuu��e	ܛ� "��D$c���!�����3&�Q9��8���#9�+U���vZ�_�e�$���<�� ���W�8��F;��7�<�"�uc��	؜��&��[2?W�$�3�4b"X�KG�ܙr�P6ƁF�_����֭W/��5���F�V�Q�"JH�+2X6��MA6'S�b4����������YU���-ύ�4�l���aY�,��8���Z����L���� '#��G	��'6d��(6�O�և���$T��@u�u��,[����h8U>"�#�q��� �ą}����Ni�Ê���zR�$�jY4����~�p�x<1����1�+딳 E�dD��2XiU�f��Y(K��Y(%�	�v�9vN��,�Z�2ٹ���{a�i>�i���4�yc��VX�ĺk�N*�϶P[����t�|�2����� M���@I�S�'�ߞZ`Y6���������T
�qZP�W��!�Qs��6O�EM�D�<dcEFQ��I7-�7��֛_ޅ�D�pN���n����sO^j����L֪=y��~@�>�r��Um���]Ґ�q�t��6�>�ѡ�nx��[��\�G�Y�Gf
{q3�!�,J���)��-Y�2|��~��,�/���C�{[i�����_bPPQL�S7�/��X�q��Q�{R���!z�����q��fsU�d��!�pS��ee�5Y�
$co���l6���     