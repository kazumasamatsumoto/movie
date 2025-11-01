#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

FEATURES: dict[str, dict[str, object]] = {
    "default": {
        "feature_name": "`satisfies`演算子",
        "empathy": "こういう型ハプニング、現場で必ず誰かが体験していますよね",
        "tech": "`satisfies`でオブジェクトリテラルの構造をサクッと検証できます",
        "cta_keyword": "あるある報告",
        "doc_keywords": "`satisfies`, `TypeScript 5.9`, 型安全",
        "doc_notes": "汎用パターン。必要に応じて会話のディテールを足してください。",
        "doc_tone": "テンポの良い共感ボケと冷静ツッコミ",
        "code": [
            """type User = {
  id: string;
  role?: "admin" | "editor";
};

const candidate = { id: "u1", role: "admin" };""",
            """const strictUser = {
  id: "u1",
  role: "editor",
} satisfies User;

strictUser.role.toUpperCase();""",
            """function ensureUser(user: User) {
  if (!user.role) {
    throw new Error("role required");
  }
  return user;
}""",
        ],
    },
    "any_escape": {
        "feature_name": "`unknown` + `satisfies`コンボ",
        "empathy": "一度`any`で逃げるとレビューで永遠に突っ込まれますからね",
        "tech": "`unknown`で受けて`satisfies`で構造を固定すると安心です",
        "cta_keyword": "any卒業宣言",
        "doc_keywords": "`unknown`, `satisfies`, `any`",
        "doc_notes": "レガシーAPIからの脱出をテーマにすると刺さりやすいです。",
        "doc_tone": "自虐多めでレビュー戦線を語る",
        "code": [
            """function fetchLegacy(): any {
  return { id: "u1", role: "admin" };
}

const rawUser = fetchLegacy();
const rawRole = rawUser.role;""",
            """type StrictUser = {
  id: string;
  role: "admin" | "editor";
};

const normalized = {
  id: rawUser.id,
  role: rawUser.role ?? "editor",
} satisfies StrictUser;""",
            """function ensureStrict(user: StrictUser) {
  return `${user.id}:${user.role}`;
}

console.log(ensureStrict(normalized));""",
        ],
    },
    "never_check": {
        "feature_name": "網羅性チェック関数",
        "empathy": "`never`絡みのエラーは理解した途端にまた忘れちゃいますよね",
        "tech": "判別ユニオンと`never`チェックで抜け漏れを強制できます",
        "cta_keyword": "never迷子",
        "doc_keywords": "`never`, 判別ユニオン, 網羅性",
        "doc_notes": "switch文での網羅性保証を軽く触れる構成が合います。",
        "doc_tone": "理屈は冷静に、リアクションは大げさに",
        "code": [
            """type Status = "draft" | "review" | "done";

function assertNever(x: never): never {
  throw new Error(`unexpected status: ${x}`);
}""",
            """function handleStatus(status: Status) {
  switch (status) {
    case "draft":
      return "WIP";
    case "review":
      return "Reviewing";
    case "done":
      return "Released";
    default:
      assertNever(status);
  }
}""",
            """const result = handleStatus("draft");
console.log(result);

handleStatus("done");""",
        ],
    },
    "inference": {
        "feature_name": "型推論のヒント付け",
        "empathy": "推論任せにすると意図しない型になって焦りますよね",
        "tech": "ジェネリック制約や`infer`で推論を落ち着かせられます",
        "cta_keyword": "推論あるある",
        "doc_keywords": "型推論, ジェネリクス制約, `infer`",
        "doc_notes": "ジェネリクスを怖がらず使うコツとしてまとめると良いです。",
        "doc_tone": "焦りながらも冷静に仕組みを語る",
        "code": [
            """function first<T extends { id: string }>(list: T[]) {
  return list[0];
}

const users = [{ id: "u1", name: "m" }];
const firstUser = first(users);""",
            """type ExtractName<T> = T extends { name: infer N } ? N : never;

type Name = ExtractName<typeof firstUser>;
const upper = (firstUser.name as Name).toUpperCase();""",
            """function ensureName(name: string) {
  return name.length;
}

ensureName(upper);""",
        ],
    },
    "as_const": {
        "feature_name": "`as const`リテラル固定",
        "empathy": "リテラルが勝手に`string`に昇格するとイラッとしますよね",
        "tech": "`as const`で意図したユニオンをキープできます",
        "cta_keyword": "asconst派",
        "doc_keywords": "`as const`, リテラル型, 推論制御",
        "doc_notes": "配列とオブジェクト両方の例を入れると喜ばれます。",
        "doc_tone": "小ネタを畳みかけるテンポ",
        "code": [
            """const roles = ["admin", "editor"] as const;

function accept(role: (typeof roles)[number]) {
  return role.toUpperCase();
}

accept("admin");""",
            """const config = {
  mode: "dark",
  retries: 3,
} as const;

type Mode = typeof config.mode;""",
            """function pickFlag<T extends readonly string[]>(flags: T) {
  return flags[0];
}

pickFlag(roles);""",
        ],
    },
    "satisfies": {
        "feature_name": "`satisfies`による型映え",
        "empathy": "`satisfies`を盛り過ぎて怒られた経験、誰しもありますよね",
        "tech": "リテラル表現と構造チェックを両立できるのが強みです",
        "cta_keyword": "satisfies勢",
        "doc_keywords": "`satisfies`, 構造チェック, リテラル",
        "doc_notes": "`as`との違いをネタにすると共感が増します。",
        "doc_tone": "ドヤ顔とツッコミの温度差で笑いを作る",
    },
    "record": {
        "feature_name": "`Record`ユーティリティ",
        "empathy": "`Record<string, unknown>`を見るとちょっと不安になりますよね",
        "tech": "リテラルキーを組み合わせて現場に馴染む辞書型へ整えられます",
        "cta_keyword": "record地獄",
        "doc_keywords": "`Record`, リテラルキー, マップ型",
        "doc_notes": "`as const`との連携を添えると分かりやすいです。",
        "doc_tone": "帳票整理みたいなノリでテンポ良く",
        "code": [
            """const roleMap: Record<"admin" | "editor", number> = {
  admin: 1,
  editor: 2,
};

const label = roleMap.admin;""",
            """type FlagMap = Record<string, boolean>;

const flags: FlagMap = { feature: true };
flags.beta = false;""",
            """const typedFlags = {
  feature: true,
  beta: false,
} satisfies Record<string, boolean>;""",
        ],
    },
    "partial": {
        "feature_name": "ユーティリティ型の組み合わせ",
        "empathy": "`Pick`と`Omit`でパーツを組むと脳が絡まりますよね",
        "tech": "`Partial`と組み合わせて差分型を安全に構築できます",
        "cta_keyword": "ユーティリティ職人",
        "doc_keywords": "`Pick`, `Partial`, DTO",
        "doc_notes": "フォーム更新やDTO差分をイメージすると現場感が出ます。",
        "doc_tone": "組み立て作業を笑いに変える",
        "code": [
            """type User = { id: string; name: string; role: string };

type UserUpdate = Partial<Pick<User, "name" | "role">>;

const update: UserUpdate = { role: "admin" };""",
            """function applyUpdate(user: User, patch: UserUpdate): User {
  return { ...user, ...patch };
}

const next = applyUpdate({ id: "1", name: "a", role: "user" }, update);""",
            """type WithoutRole = Omit<User, "role">;

const base: WithoutRole = { id: "1", name: "a" };""",
        ],
    },
    "readonly": {
        "feature_name": "`Readonly`と`Mutable`の切替",
        "empathy": "読み取り専用にした途端 push したくなるんですよね",
        "tech": "`Readonly`で守って必要な箇所だけ`Mutable`化できます",
        "cta_keyword": "readonly封印",
        "doc_keywords": "`Readonly`, `ReadonlyArray`, ミューテーション",
        "doc_notes": "イミュータブル戦争を茶化すとウケが良いです。",
        "doc_tone": "イミュータブル信者と現場派の温度差",
        "code": [
            """type User = { id: string; tags: string[] };

const frozen: Readonly<User> = { id: "1", tags: ["ts"] };
// frozen.tags.push("js"); // エラー""",
            """type Mutable<T> = {
  -readonly [K in keyof T]: T[K];
};

const mutable: Mutable<typeof frozen> = { ...frozen };
mutable.tags.push("js");""",
            """const tags: ReadonlyArray<string> = ["ts", "js"];
const copied = [...tags];
copied.push("rust");""",
        ],
    },
    "unknown": {
        "feature_name": "`unknown`ガード",
        "empathy": "`unknown`を`any`に戻したくなる誘惑と戦い続けますよね",
        "tech": "型ガードで`unknown`を段階的に狭めれば安心です",
        "cta_keyword": "unknown攻略",
        "doc_keywords": "`unknown`, 型ガード, `in`演算子",
        "doc_notes": "ユーザー入力や外部API検証を想定すると共感度が高いです。",
        "doc_tone": "慎重派と雑派のギャップで笑う",
        "code": [
            """function isUser(value: unknown): value is { id: string } {
  return typeof value === "object" && value !== null && "id" in value;
}

const maybeUser: unknown = JSON.parse('{"id":"1"}');""",
            """if (isUser(maybeUser)) {
  console.log(maybeUser.id);
} else {
  console.warn("not user");
}""",
            """const safeUser = maybeUser as unknown;
// safeUser.id; // NG: まだunknown""",
        ],
    },
    "tsconfig": {
        "feature_name": "`tsconfig`整備",
        "empathy": "tsconfigを触ると一晩溶けるのはあるあるですよね",
        "tech": "`extends`や`include`を整理するとビルドが安定します",
        "cta_keyword": "tsconfig地獄",
        "doc_keywords": "tsconfig, extends, compilerOptions",
        "doc_notes": "設定ファイル迷子ネタで攻めるとコメントが集まりやすいです。",
        "doc_tone": "設定ファイルに疲弊しつつも冷静に指南",
        "code": [
            """// tsconfig.base.json
{
  "compilerOptions": {
    "strict": true,
    "module": "esnext"
  }
}""",
            """// tsconfig.app.json
{
  "extends": "./tsconfig.base.json",
  "include": ["src"],
  "exclude": ["dist"]
}""",
            """// package.json
{
  "scripts": {
    "build": "tsc -p tsconfig.app.json"
  }
}""",
        ],
    },
    "generics": {
        "feature_name": "ジェネリクスの制約",
        "empathy": "ジェネリクスを重ねると誰も読めなくなるんですよね",
        "tech": "`extends`やデフォルト型で読みやすさを保てます",
        "cta_keyword": "ジェネリクス沼",
        "doc_keywords": "ジェネリクス, 制約, デフォルト型",
        "doc_notes": "型設計のバランス感覚を語ると刺さります。",
        "doc_tone": "数学っぽさを軽く茶化す",
        "code": [
            """type Loader<T extends string = "json"> = {
  type: T;
  load: () => Promise<unknown>;
};

const jsonLoader: Loader = { type: "json", load: async () => ({}) };""",
            """function useLoader<T extends Loader>(loader: T) {
  return loader.load();
}

useLoader(jsonLoader);
useLoader({ type: "csv", load: async () => [] });""",
            """type ExtractType<T extends Loader> = T["type"];

type JsonType = ExtractType<typeof jsonLoader>;""",
        ],
    },
    "template_literal": {
        "feature_name": "テンプレートリテラル型",
        "empathy": "Template Literal型で遊びすぎると未来の自分が読めなくなりますよね",
        "tech": "接頭辞・接尾辞を束ねて安全なキーを作れます",
        "cta_keyword": "テンリテ職人",
        "doc_keywords": "Template Literal, キー生成, 型操作",
        "doc_notes": "key remapやコード規約に絡めると面白いです。",
        "doc_tone": "言葉遊びトーンで小気味良く",
        "code": [
            """type EventName = `on${Capitalize<string>}`;

type UserEvent = `user:${"created" | "updated"}`;

const event: UserEvent = "user:created";""",
            """type WithPrefix<T extends string> = `app:${T}`;

type Routes = WithPrefix<"login" | "home">;

const route: Routes = "app:login";""",
            """type ExtractSuffix<T extends string> = T extends `${string}:${infer R}` ? R : never;

type Action = ExtractSuffix<UserEvent>;
const action: Action = "updated";""",
        ],
    },
    "async": {
        "feature_name": "`Awaited`と非同期型整備",
        "empathy": "Promiseチェーンを追ってると朝を迎えますよね",
        "tech": "`Awaited`で戻り値を先に取り出しておくと安心です",
        "cta_keyword": "非同期迷子",
        "doc_keywords": "Promise, `Awaited`, 非同期",
        "doc_notes": "APIレスポンス整形やoptional chainingの話題を混ぜやすいです。",
        "doc_tone": "深夜デバッグ感を演出",
        "code": [
            """async function fetchUser() {
  return { id: "1", name: "m" };
}

type UserPromise = ReturnType<typeof fetchUser>;
type User = Awaited<UserPromise>;""",
            """async function load() {
  const user: User = await fetchUser();
  return user.name?.toUpperCase();
}

load().then(console.log);""",
            """type Fetcher<T> = () => Promise<T>;

function mapFetcher<T, U>(fn: Fetcher<T>, map: (value: T) => U): Fetcher<U> {
  return async () => map(await fn());
}""",
        ],
    },
    "module": {
        "feature_name": "モジュール解像度の整理",
        "empathy": "ESMとCJSの狭間で迷子になるのは週間行事ですよね",
        "tech": "`module`と`moduleResolution`を合わせて揃えるのが近道です",
        "cta_keyword": "module迷子",
        "doc_keywords": "ESM, CJS, moduleResolution",
        "doc_notes": "import/exportの辛さを笑いに変える構成がハマります。",
        "doc_tone": "混乱を笑いに変えるカオス系",
        "code": [
            """// tsconfig.json
{
  "compilerOptions": {
    "module": "esnext",
    "moduleResolution": "bundler"
  }
}""",
            """// package.json
{
  "type": "module",
  "scripts": {
    "dev": "tsx src/index.ts"
  }
}""",
            """import { readFile } from "node:fs/promises";

async function main() {
  const pkg = await readFile("package.json", "utf8");
  console.log(pkg.length);
}

main();""",
        ],
    },
    "schema": {
        "feature_name": "スキーマ&型同期",
        "empathy": "Zod派とio-ts派で永遠に議論しがちですよね",
        "tech": "ランタイムスキーマとTypeScript型を一元管理できます",
        "cta_keyword": "スキーマ派",
        "doc_keywords": "Zod, io-ts, スキーマ定義",
        "doc_notes": "バリデーションと型の二重管理をネタにすると映えます。",
        "doc_tone": "宗派争いを笑いに変える",
        "code": [
            """import { z } from "zod";

const userSchema = z.object({ id: z.string(), role: z.enum(["admin", "editor"]) });

type User = z.infer<typeof userSchema>;""",
            """const parsed = userSchema.parse({ id: "u1", role: "admin" });

function handle(user: User) {
  return user.role.toUpperCase();
}""",
            """// io-tsなら
// import * as t from "io-ts";
// const UserCodec = t.type({ id: t.string });""",
        ],
    },
    "structure": {
        "feature_name": "型エイリアス整理術",
        "empathy": "`interface`派と`type`派の争いは終わりませんよね",
        "tech": "用途ごとに使い分けるとレビューが静かになります",
        "cta_keyword": "型派閥",
        "doc_keywords": "interface, type alias, 命名規則",
        "doc_notes": "派閥ネタ＋実務ルールを絡めるとコメントが伸びます。",
        "doc_tone": "派閥会議風の軽口",
        "code": [
            """interface User {
  id: string;
  name: string;
}

type UserDto = Pick<User, "id" | "name">;""",
            """type Handler = (user: User) => void;

const handler: Handler = user => {
  console.log(user.id);
};""",
            """interface Service {
  fetch(id: string): Promise<User>;
}

const service: Service = {
  async fetch(id) {
    return { id, name: "m" };
  },
};""",
        ],
    },
    "decorator": {
        "feature_name": "デコレータ設定",
        "empathy": "デコレータONにした瞬間ビルドが怒りますよね",
        "tech": "`experimentalDecorators`と`emitDecoratorMetadata`を揃えましょう",
        "cta_keyword": "デコレータ派",
        "doc_keywords": "decorators, emitDecoratorMetadata, tsconfig",
        "doc_notes": "設定と実装の両面をさらっと紹介すると親切です。",
        "doc_tone": "設定と実装の二刀流あるある",
        "code": [
            """// tsconfig.json
{
  "compilerOptions": {
    "experimentalDecorators": true,
    "emitDecoratorMetadata": true
  }
}""",
            """function Log(): MethodDecorator {
  return (_target, _key, descriptor) => {
    const fn = descriptor.value as Function;
    descriptor.value = function (...args: unknown[]) {
      console.log("call", args);
      return fn.apply(this, args);
    };
  };
}""",
            """class Service {
  @Log()
  run() {
    return "ok";
  }
}

new Service().run();""",
        ],
    },
    "react": {
        "feature_name": "React型の型注釈",
        "empathy": "`useState<string | null>`って書くか悩みますよね",
        "tech": "初期値とジェネリクス指定で推論を合わせられます",
        "cta_keyword": "React型談義",
        "doc_keywords": "React, useState, JSX",
        "doc_notes": "React Hook周りの型ギャップを笑いに変えましょう。",
        "doc_tone": "開発会話っぽく軽快に",
        "code": [
            """import { useState } from "react";

const [value, setValue] = useState<string | null>(null);
setValue("ready");
setValue(null);""",
            """type Props = {
  status: "idle" | "loading" | "done";
};

const Badge = ({ status }: Props) => <span>{status}</span>;""",
            """type ClickHandler = React.MouseEventHandler<HTMLButtonElement>;

const handleClick: ClickHandler = event => {
  event.preventDefault();
};""",
        ],
    },
    "angular": {
        "feature_name": "Angular型の共有",
        "empathy": "Angularの型、DIまわりで一気に崩れがちですよね",
        "tech": "`Readonly`やDTOを駆使してサービス間で型を共有しましょう",
        "cta_keyword": "Angular勢",
        "doc_keywords": "Angular, DTO, DI",
        "doc_notes": "サービス層とコンポーネントの連携を描くと臨場感が出ます。",
        "doc_tone": "現場愚痴を軽快に",
        "code": [
            """import { Injectable } from "@angular/core";

type Todo = {
  id: string;
  title: string;
  done: boolean;
};

@Injectable({ providedIn: "root" })
export class TodoService {}""",
            """type CreateTodoDto = Pick<Todo, "title">;

function toDto(todo: Todo): Readonly<CreateTodoDto> {
  return { title: todo.title };
}""",
            """const list: ReadonlyArray<Todo> = [];
const first = list[0];
console.log(first?.title);""",
        ],
    },
    "nest": {
        "feature_name": "Nest.js DTO管理",
        "empathy": "DTOの型ズレが本番で出て震えた経験ありますよね",
        "tech": "`PickType`や`PartialType`で使い回しができます",
        "cta_keyword": "Nest型運用",
        "doc_keywords": "Nest.js, DTO, class-transformer",
        "doc_notes": "classベースDTOの再利用をネタにすると刺さります。",
        "doc_tone": "バックエンド現場ノリ",
        "code": [
            """import { PartialType } from "@nestjs/mapped-types";

class CreateUserDto {
  id!: string;
  name!: string;
}

class UpdateUserDto extends PartialType(CreateUserDto) {}""",
            """function toEntity(dto: CreateUserDto) {
  return { ...dto, createdAt: new Date() };
}

console.log(toEntity({ id: "1", name: "m" }));""",
            """type UserResponse = Readonly<CreateUserDto>;

const res: UserResponse = { id: "1", name: "m" };""",
        ],
    },
    "lint": {
        "feature_name": "Lintと型チェックの住み分け",
        "empathy": "Lintを厳しくするとCIが赤く染まりますよね",
        "tech": "`eslint --max-warnings 0`と`tsc --noEmit`を役割分担させましょう",
        "cta_keyword": "Lint警察",
        "doc_keywords": "ESLint, tsc --noEmit, CI",
        "doc_notes": "Lintルールと型チェッカーの線引きで盛り上げます。",
        "doc_tone": "CI担当の叫びを代弁",
        "code": [
            """// package.json
{
  "scripts": {
    "lint": "eslint ./src --max-warnings=0",
    "typecheck": "tsc --noEmit"
  }
}""",
            """// .eslintrc.cjs
module.exports = {
  extends: ["plugin:@typescript-eslint/recommended"],
  rules: {
    "@typescript-eslint/no-explicit-any": "warn"
  }
};""",
            """// CI設定例
yarn lint

yarn typecheck""",
        ],
    },
    "tooling": {
        "feature_name": "ビルドツール整備",
        "empathy": "`tsc --watch`に人生預けた瞬間ありますよね",
        "tech": "`incremental`や`ts-node`を使い分けて快適にしましょう",
        "cta_keyword": "ビルド班",
        "doc_keywords": "tsc --watch, incremental, ts-node",
        "doc_notes": "開発体験とビルド速度の葛藤を描きましょう。",
        "doc_tone": "DevOpsっぽい愚痴",
        "code": [
            """// tsconfig.json
{
  "compilerOptions": {
    "incremental": true,
    "tsBuildInfoFile": ".tsbuildinfo"
  }
}""",
            """// package.json
{
  "scripts": {
    "dev": "ts-node --esm src/index.ts",
    "build": "tsc -p tsconfig.json"
  }
}""",
            """import "ts-node/register";

console.log("dev server ready");

// nodemon --exec ts-node src/index.ts""",
        ],
    },
    "orchestration": {
        "feature_name": "モノレポ型共有",
        "empathy": "ワークスペース設定が噛み合わなくて朝になるのはあるあるですよね",
        "tech": "`pnpm`や`yarn`のworkspaceで型パッケージを共有しましょう",
        "cta_keyword": "workspace迷子",
        "doc_keywords": "pnpm workspace, モノレポ, 型共有",
        "doc_notes": "型パッケージをどう配るかの苦労話がフィットします。",
        "doc_tone": "リードエンジニアの嘆き風",
        "code": [
            """# pnpm-workspace.yaml
packages:
  - packages/*
  - apps/*""",
            """// packages/types/package.json
{
  "name": "@app/types",
  "version": "1.0.0",
  "types": "index.d.ts"
}""",
            """// apps/web/package.json
{
  "dependencies": {
    "@app/types": "workspace:*"
  }
}""",
        ],
    },
    "schema_api": {
        "feature_name": "APIレスポンス型の整備",
        "empathy": "APIレスポンス型を手書きするのツライですよね",
        "tech": "ジェネリクスとスキーマ生成で自動化できます",
        "cta_keyword": "API型管理",
        "doc_keywords": "Axios, Fetch, API型",
        "doc_notes": "HTTPクライアントの型付けに触れて共感を誘います。",
        "doc_tone": "バックエンド連携の愚痴を楽しく",
        "code": [
            """import axios from "axios";

type ApiResponse<T> = Promise<{ data: T }>;

function getUser(): ApiResponse<{ id: string }> {
  return axios.get("/user");
}""",
            """type ExtractData<T> = T extends Promise<{ data: infer D }> ? D : never;

type User = ExtractData<ReturnType<typeof getUser>>;""",
            """async function main() {
  const res = await getUser();
  console.log(res.data.id);
}

main();""",
        ],
    },
    "result": {
        "feature_name": "Result型パターン",
        "empathy": "Result型を導入したら関数定義が長くなりがちですよね",
        "tech": "ジェネリクスと判別ユニオンで安全な結果型を扱えます",
        "cta_keyword": "Result派",
        "doc_keywords": "Result型, 判別ユニオン",
        "doc_notes": "エラーハンドリング改善ネタとしてまとめましょう。",
        "doc_tone": "関数戻り値で盛り上がる",
        "code": [
            """type Result<T, E> = { ok: true; value: T } | { ok: false; error: E };

function success<T>(value: T): Result<T, never> {
  return { ok: true, value };
}""",
            """function failure<E>(error: E): Result<never, E> {
  return { ok: false, error };
}

const value = success(42);
const error = failure(new Error("boom"));""",
            """function unwrap<T, E>(result: Result<T, E>): T {
  if (!result.ok) {
    throw result.error;
  }
  return result.value;
}

unwrap(value);""",
        ],
    },
    "error": {
        "feature_name": "エラー型設計",
        "empathy": "Error型をどう表現するか議論が終わりませんよね",
        "tech": "独自エラー型をユニオンで整理すると読みやすくなります",
        "cta_keyword": "エラー設計",
        "doc_keywords": "Error型, カスタムエラー, 判別ユニオン",
        "doc_notes": "失敗談を混ぜるとコメント欄が盛り上がります。",
        "doc_tone": "失敗談を面白く語る",
        "code": [
            """type AppError =
  | { type: "Network"; message: string }
  | { type: "Validation"; field: string };

const err: AppError = { type: "Network", message: "timeout" };""",
            """function handleError(error: AppError) {
  switch (error.type) {
    case "Network":
      return `retry: ${error.message}`;
    case "Validation":
      return `fix field: ${error.field}`;
  }
}""",
            """function toError(e: unknown): AppError {
  if (e instanceof Error) {
    return { type: "Network", message: e.message };
  }
  return { type: "Validation", field: "unknown" };
}""",
        ],
    },
    "enum": {
        "feature_name": "リテラルvs enumの使い分け",
        "empathy": "enumとリテラルどっち派か永遠に議論になりますよね",
        "tech": "`as const`とユニオンで軽量に表現できます",
        "cta_keyword": "enum派閥",
        "doc_keywords": "enum, literal union, as const",
        "doc_notes": "派閥トークに実例を添えて笑いを誘いましょう。",
        "doc_tone": "派閥バトル風",
        "code": [
            """enum RoleEnum {
  Admin = "admin",
  Editor = "editor",
}

const roleFromEnum: RoleEnum = RoleEnum.Admin;""",
            """const roles = ["admin", "editor"] as const;

type RoleLiteral = (typeof roles)[number];

const role: RoleLiteral = "admin";""",
            """function toLabel(role: RoleLiteral) {
  return role === "admin" ? "管理者" : "編集";
}

toLabel(role);""",
        ],
    },
    "union": {
        "feature_name": "判別ユニオン設計",
        "empathy": "Unionが巨大化するとフォーマッタが泣きますよね",
        "tech": "判別キーを入れて`switch`で安全に処理できます",
        "cta_keyword": "union整理",
        "doc_keywords": "判別ユニオン, switch, never",
        "doc_notes": "ケース分けの苦労を共有すると盛り上がります。",
        "doc_tone": "バグ修正あるあるテンポ",
        "code": [
            """type Event =
  | { type: "click"; x: number; y: number }
  | { type: "submit"; formId: string };

function handle(event: Event) {
  if (event.type === "click") {
    console.log(event.x, event.y);
  }
}""",
            """function exhaust(event: Event) {
  switch (event.type) {
    case "click":
      return "clicked";
    case "submit":
      return "submitted";
    default:
      const neverEvent: never = event;
      return neverEvent;
  }
}""",
            """const submit: Event = { type: "submit", formId: "main" };
console.log(handle(submit));""",
        ],
    },
    "date": {
        "feature_name": "`Date`型ラップ",
        "empathy": "Date型を扱うときライブラリ探しの旅に出がちですよね",
        "tech": "値オブジェクトとISO文字列で往復させましょう",
        "cta_keyword": "Date管理",
        "doc_keywords": "Date型, ISO, 値オブジェクト",
        "doc_notes": "時刻処理のつらさをネタ化すると共感が集まります。",
        "doc_tone": "時間泥棒に怒るノリ",
        "code": [
            """type IsoDate = string;

function toIso(date: Date): IsoDate {
  return date.toISOString();
}

const nowIso = toIso(new Date());""",
            """function fromIso(value: IsoDate): Date {
  return new Date(value);
}

const restored = fromIso(nowIso);
console.log(restored.getUTCFullYear());""",
            """type Timeline = {
  createdAt: IsoDate;
  updatedAt: IsoDate;
};

const timeline: Timeline = { createdAt: nowIso, updatedAt: nowIso };""",
        ],
    },
    "types_publish": {
        "feature_name": "型配布フロー",
        "empathy": "型定義の配布で`types`指定を忘れて炎上したことありますよね",
        "tech": "`types`とバンドラのdts出力を合わせれば安全に公開できます",
        "cta_keyword": "型配布完了",
        "doc_keywords": "型配布, publishConfig, dts",
        "doc_notes": "npm公開や社内レジストリ共有の苦労話を絡めると◎。",
        "doc_tone": "リリース直前のバタバタ感で魅せる",
        "code": [
            """// package.json
{
  "name": "@scope/lib",
  "version": "1.0.0",
  "types": "dist/index.d.ts"
}""",
            """// tsup.config.ts
import { defineConfig } from "tsup";

export default defineConfig({
  dts: true,
  clean: true,
});""",
            """export type Service = {
  run(): Promise<void>;
};

export const createService = (): Service => ({
  async run() {},
});""",
        ],
    },
}

DEFAULT = FEATURES["default"]
for data in FEATURES.values():
    data.setdefault("code", DEFAULT["code"])
    data.setdefault("doc_tone", DEFAULT["doc_tone"])
    data.setdefault("doc_notes", DEFAULT["doc_notes"])
    data.setdefault("doc_keywords", DEFAULT["doc_keywords"])
    data.setdefault("cta_keyword", DEFAULT["cta_keyword"])
    data.setdefault("empathy", DEFAULT["empathy"])
    data.setdefault("tech", DEFAULT["tech"])

KEYWORD_FEATURE_MAP: list[tuple[list[str], str]] = [
    (["any"], "any_escape"),
    (["never"], "never_check"),
    (["推論", "infer"], "inference"),
    (["as const"], "as_const"),
    (["satisfies"], "satisfies"),
    (["record"], "record"),
    (["partial", "pick", "omit", "dto", "deeppartial", "deeppartial", "deepreadonly"], "partial"),
    (["readonlyarray", "readonly", "mutable"], "readonly"),
    (["strictnullchecks", "unknown", "nounchecked", "nonnullable", "nullable"], "unknown"),
    (["tsconfig", "moduleresolution", "paths", "verbatimmodule", "modulesuffixes", "resolvejsonmodule", "emitdecorator", "noimplicitany", "tsbuildinfo", "isolatedmodules"], "tsconfig"),
    (["generics", "extends", "conditional", "variance", "variadic", "mapped", "strictbindcallapply", "type predicate"], "generics"),
    (["template literal", "テンプレート", "keyremap", "literal型"], "template_literal"),
    (["awaited", "async", "promise", "optional chaining", "flatmap", "promiselike"], "async"),
    (["enum"], "enum"),
    (["union", "判別", "exhaustive"], "union"),
    (["zod", "io-ts", "json-schema", "schema", "openapi", "drizzle", "prisma"], "schema"),
    (["interface派", "type派", "interface vs", "type エイリアス", "type alias"], "structure"),
    (["decorator"], "decorator"),
    (["react", "jsx", "usestate", "next.js", "useState"], "react"),
    (["angular"], "angular"),
    (["nest"], "nest"),
    (["eslint", "lint", "max-warnings", "noemit", "dprint", "prettier", "import/order"], "lint"),
    (["@types", "publishconfig", "tsup", "types\":", "type-fest", "tslib"], "types_publish"),
    (["axios", "fetch", "api", "http"], "schema_api"),
    (["project references", "monorepo", "workspace", "pnpm", "yarn", "npm"], "orchestration"),
    (["ts-node", "tsc", "--watch", "build"], "tooling"),
    (["result"], "result"),
    (["error"], "error"),
    (["date"], "date"),
    (["esm", "cjs", "import type", "barrel"], "module"),
]


def parse_titles(path: Path) -> list[str]:
    pattern = re.compile(r"^\\s*\\d+\\.\\s+「(.+)」")
    titles: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        match = pattern.match(line)
        if match:
            titles.append(match.group(1))
    return titles


def choose_feature(title: str) -> dict[str, object]:
    lower = title.lower()
    for keywords, feature_id in KEYWORD_FEATURE_MAP:
        if any(keyword in lower for keyword in keywords):
            return FEATURES[feature_id]
    return DEFAULT


def build_daihon(index: int, title: str, feature: dict[str, object]) -> str:
    cta_keyword = feature["cta_keyword"]
    lines = [
        f"ずんだもん「【導入】TypeScript書いてるとさ、{title}って絶対あるよね？」",
        f"四国めたん「【共感】わかります。{feature['empathy']}」",
        f"ずんだもん「【描写】しかも{title}が起きると、チーム全員が無言になるんだよ！」",
        f"四国めたん「【技術ネタ】それならTypeScriptの{feature['feature_name']}を使えば、{feature['tech']}」",
        f"ずんだもん「【オチ】いや待って、対策すると{title}第2ラウンドが始まるやつ！」",
        f"四国めたん「【締め】共感した方は“{cta_keyword}”ってコメントで教えてください！」",
        "ずんだもん「【CTA】あなたのTypeScriptあるあるも募集中だよ！」",
    ]
    code_block = "\n\n".join(feature["code"])  # type: ignore[arg-type]
    return (
        f"# #{index:03} 「{title}」台本\n\n"
        + "\n".join(lines)
        + "\n\n---\n\n## 📺 画面表示用コード\n\n```typescript\n"
        + code_block
        + "\n```"
    )


def build_document(index: int, title: str, feature: dict[str, object]) -> str:
    return (
        f"# #{index:03} 「{title}」制作メモ\n\n"
        f"- **想定シーン**: {title}に遭遇した瞬間の愚痴を切り取る\n"
        f"- **狙いトーン**: {feature['doc_tone']}\n"
        f"- **技術キーワード**: {feature['doc_keywords']}\n"
        f"- **使いたい一言**: 「{feature['cta_keyword']}」\n"
        f"- **CTA案**: コメントで「{feature['cta_keyword']}」と書いてもらい、似た体験を募る\n"
        f"- **備考**: {feature['doc_notes']}\n"
    )


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    title_path = Path(base_dir.parent, "aruaru-titles.md")
    daihon_dir = base_dir / "daihon"
    document_dir = base_dir / "document"

    titles = parse_titles(title_path)
    if not titles:
        raise SystemExit("タイトルが見つかりませんでした。")

    daihon_dir.mkdir(parents=True, exist_ok=True)
    document_dir.mkdir(parents=True, exist_ok=True)

    for index, title in enumerate(titles, start=1):
        feature = choose_feature(title)
        daihon_path = daihon_dir / f"{index:03}.md"
        document_path = document_dir / f"{index:03}.md"
        daihon_path.write_text(build_daihon(index, title, feature), encoding="utf-8")
        document_path.write_text(build_document(index, title, feature), encoding="utf-8")


if __name__ == "__main__":
    main()
