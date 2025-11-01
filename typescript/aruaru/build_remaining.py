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
        "doc_keywords": "`satisfies`, TypeScript 5.9, 型安全",
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
        "empathy": "`any`で逃げた翌日にレビューが真っ赤になりますからね",
        "tech": "`unknown`で受けて`satisfies`で構造を固定すると安心です",
        "cta_keyword": "any卒業宣言",
        "doc_keywords": "`unknown`, `satisfies`, `any`",
        "doc_notes": "レガシーAPIや暫定対応の文脈で語ると共感を得やすい。",
        "doc_tone": "自虐多めでレビュー戦線を語る",
        "code": [
            """function fetchLegacy(): any {
  return { id: "u1", role: "admin" };
}

const rawUser = fetchLegacy();""",
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
    "never": {
        "feature_name": "網羅性チェック",
        "empathy": "`never`絡みのエラーは理解した翌日に忘れちゃいますよね",
        "tech": "判別ユニオンと`assertNever`を仕込めば漏れを自動で炙り出せます",
        "cta_keyword": "never迷子",
        "doc_keywords": "`never`, 判別ユニオン, 網羅性",
        "doc_notes": "switch文での網羅性保証を短く扱うと伝わりやすい。",
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
            """handleStatus("draft");
handleStatus("done");""",
        ],
    },
    "inference": {
        "feature_name": "型推論のヒント付け",
        "empathy": "推論任せにすると意図しない型になって焦りますよね",
        "tech": "ジェネリクス制約や型ガードを足せば推論が安定します",
        "cta_keyword": "推論あるある",
        "doc_keywords": "型推論, ジェネリクス制約, `infer`",
        "doc_notes": "ジェネリクスを怖がらず使うコツとしてまとめると良いです。",
        "doc_tone": "焦りながらも冷静に仕組みを語る",
        "code": [
            """type User = { id: string; name?: string };

function hasName(user: User): user is User & { name: string } {
  return typeof user.name === "string";
}""",
            """function firstWithName<T extends User>(items: readonly T[]) {
  const target = items.find(hasName);
  if (!target) throw new Error("name missing");
  return target;
}

const users = [{ id: "u1", name: "m" }];
const firstUser = firstWithName(users);""",
            """type Name = typeof firstUser.name;

function shout(name: Name) {
  return name.toUpperCase();
}

shout(firstUser.name);""",
        ],
    },
    "as_const": {
        "feature_name": "`as const`リテラル固定",
        "empathy": "リテラルが勝手に`string`に昇格するとイラッとしますよね",
        "tech": "`as const`で配列もオブジェクトも一気にリテラル固定できます",
        "cta_keyword": "asconst派",
        "doc_keywords": "`as const`, リテラル型, 推論制御",
        "doc_notes": "配列とオブジェクトの両方を例示すると伝わりやすい。",
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
        "empathy": "`satisfies`を盛りすぎて怒られた経験、誰しもありますよね",
        "tech": "リテラル表現と構造チェックを両立できるのが強みです",
        "cta_keyword": "satisfies勢",
        "doc_keywords": "`satisfies`, 構造チェック, リテラル",
        "doc_notes": "`as`との違いを軽く触れると盛り上がります。",
        "doc_tone": "ドヤ顔とツッコミの温度差で笑いを作る",
        "code": [
            """type FeatureFlag = {
  mode: "strict" | "relaxed";
  retries: number;
};""",
            """const flag = {
  mode: "strict",
  retries: 3,
  debug: true,
} satisfies FeatureFlag;""",
            """function enable(flag: FeatureFlag) {
  return flag.mode.toUpperCase();
}

enable(flag);""",
        ],
    },
    "record": {
        "feature_name": "`Record`ユーティリティ",
        "empathy": "`Record<string, unknown>`を見るとちょっと不安になりますよね",
        "tech": "リテラルキーを組み合わせて現場に馴染む辞書型へ整えられます",
        "cta_keyword": "record地獄",
        "doc_keywords": "`Record`, リテラルキー, マップ型",
        "doc_notes": "`as const`との連携を添えると親切です。",
        "doc_tone": "帳票整理みたいなノリでテンポ良く",
        "code": [
            """const roleLabel: Record<"admin" | "editor", string> = {
  admin: "管理者",
  editor: "編集者",
};""",
            """const flags: Record<string, boolean> = { feature: true };
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
        "tech": "`Partial`と組み合わせて差分型を最初から用意すると整理できます",
        "cta_keyword": "ユーティリティ職人",
        "doc_keywords": "`Pick`, `Omit`, `Partial`, DTO",
        "doc_notes": "フォーム更新やDTO差分を例に出すとリアルです。",
        "doc_tone": "組み立て作業を笑いに変える",
        "code": [
            """type User = {
  id: string;
  name: string;
  role: "admin" | "editor";
};""",
            """type CreateUserDto = Pick<User, "name" | "role">;
type UpdateUserDto = Partial<CreateUserDto>;""",
            """function applyUpdate(user: User, update: UpdateUserDto): User {
  return { ...user, ...update };
}

const next = applyUpdate({ id: "1", name: "M", role: "editor" }, { role: "admin" });""",
        ],
    },
    "readonly": {
        "feature_name": "`Readonly`と`Mutable`の切替",
        "empathy": "読み取り専用にした途端 push したくなるんですよね",
        "tech": "`Readonly`で守って必要な箇所だけ`Mutable`化できます",
        "cta_keyword": "readonly封印",
        "doc_keywords": "`Readonly`, `ReadonlyArray`, ミューテーション",
        "doc_notes": "イミュータブル運用のツラさをネタにすると良い感じです。",
        "doc_tone": "イミュータブル信者と現場派の温度差",
        "code": [
            """type User = { id: string; tags: string[] };

const frozen: Readonly<User> = { id: "1", tags: ["ts"] };""",
            """type Mutable<T> = {
  -readonly [K in keyof T]: T[K];
};

const editable: Mutable<typeof frozen> = { ...frozen };
editable.tags.push("js");""",
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
}""",
            """const maybeUser: unknown = JSON.parse('{"id":"1"}');

if (isUser(maybeUser)) {
  console.log(maybeUser.id);
} else {
  console.warn("not user");
}""",
            """const safeUser = maybeUser as unknown;
// safeUser.id; // まだunknownのまま""",
        ],
    },
    "tsconfig": {
        "feature_name": "`tsconfig`整備",
        "empathy": "tsconfigを触ると一晩溶けるのはあるあるですよね",
        "tech": "`extends`や`include`を整理するとビルドが安定します",
        "cta_keyword": "tsconfig地獄",
        "doc_keywords": "tsconfig, extends, compilerOptions",
        "doc_notes": "設定ファイル迷子ネタで攻めるとコメントが集まります。",
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
    "typecheck": "tsc -p tsconfig.app.json --noEmit"
  }
}""",
        ],
    },
    "generics": {
        "feature_name": "ジェネリクス設計",
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
};""",
            """const jsonLoader: Loader = { type: "json", load: async () => ({}) };

function useLoader<T extends Loader>(loader: T) {
  return loader.load();
}

useLoader(jsonLoader);""",
            """type ExtractType<T extends Loader> = T["type"];

type LoaderType = ExtractType<typeof jsonLoader>;""",
        ],
    },
    "template_literal": {
        "feature_name": "テンプレートリテラル型",
        "empathy": "Template Literal型で遊びすぎると未来の自分が読めなくなりますよね",
        "tech": "接頭辞・接尾辞を束ねて安全なキーを作れます",
        "cta_keyword": "テンリテ職人",
        "doc_keywords": "Template Literal, キー生成, 型操作",
        "doc_notes": "key remapやディレクティブ名生成に触れると楽しいです。",
        "doc_tone": "言葉遊びトーンで小気味良く",
        "code": [
            """type EventName = `on${Capitalize<string>}`;

type UserEvent = `user:${"created" | "updated"}`;""",
            """const event: UserEvent = "user:created";

type WithPrefix<T extends string> = `app:${T}`;

type Routes = WithPrefix<"login" | "home">;""",
            """type ExtractSuffix<T extends string> = T extends `${string}:${infer R}` ? R : never;

type Action = ExtractSuffix<UserEvent>;""",
        ],
    },
    "async": {
        "feature_name": "`Awaited`と非同期型整備",
        "empathy": "Promiseチェーンを追ってると朝を迎えますよね",
        "tech": "`Awaited`で戻り値を先に取り出しておくと安心です",
        "cta_keyword": "非同期迷子",
        "doc_keywords": "Promise, `Awaited`, 非同期",
        "doc_notes": "APIレスポンス整形やoptional chainingを絡めると良いです。",
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

const userSchema = z.object({
  id: z.string(),
  role: z.enum(["admin", "editor"]),
});""",
            """type User = z.infer<typeof userSchema>;

const parsed = userSchema.parse({ id: "u1", role: "admin" });""",
            """function handle(user: User) {
  return user.role.toUpperCase();
}""",
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
    "lint": {
        "feature_name": "Lintと型チェックの住み分け",
        "empathy": "Lintを厳しくするとCIが赤く染まりますよね",
        "tech": "`eslint --max-warnings 0`と`tsc --noEmit`を役割分担させましょう",
        "cta_keyword": "Lint警察",
        "doc_keywords": "ESLint, tsc --noEmit, CI",
        "doc_notes": "Lintルールと型チェッカーの線引きをユーモラスに。",
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
            """// CI設定イメージ
yarn lint
yarn typecheck""",
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
    "orchestration": {
        "feature_name": "モノレポ型共有",
        "empathy": "ワークスペース設定が噛み合わなくて朝になるのはあるあるですよね",
        "tech": "`pnpm`や`yarn`のworkspaceで型パッケージを共有しましょう",
        "cta_keyword": "workspace迷子",
        "doc_keywords": "pnpm workspace, モノレポ, 型共有",
        "doc_notes": "型パッケージをどう配るかの苦労話がハマります。",
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
    "tooling": {
        "feature_name": "ビルドツール整備",
        "empathy": "`tsc --watch`に人生預けた瞬間ありますよね",
        "tech": "`incremental`や`ts-node`を使い分けて快適にしましょう",
        "cta_keyword": "ビルド班",
        "doc_keywords": "tsc, ts-node, incremental, build",
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
    "build": "tsc -p tsconfig.json",
    "test": "ts-jest --passWithNoTests"
  }
}""",
            """import "ts-node/register";

console.log("dev server ready");
// nodemon --exec ts-node src/index.ts""",
        ],
    },
    "result": {
        "feature_name": "Result型パターン",
        "empathy": "Result型を導入したら関数定義が長くなりがちですよね",
        "tech": "ジェネリクスと判別ユニオンで安全な結果型を扱えます",
        "cta_keyword": "Result派",
        "doc_keywords": "Result型, 判別ユニオン",
        "doc_notes": "エラーハンドリング改善ネタとして語ると効果的。",
        "doc_tone": "関数戻り値で盛り上がる",
        "code": [
            """type Result<T, E> = { ok: true; value: T } | { ok: false; error: E };""",
            """function success<T>(value: T): Result<T, never> {
  return { ok: true, value };
}

function failure<E>(error: E): Result<never, E> {
  return { ok: false, error };
}""",
            """function unwrap<T, E>(result: Result<T, E>): T {
  if (!result.ok) {
    throw result.error;
  }
  return result.value;
}

unwrap(success(42));""",
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
  | { type: "Validation"; field: string };""",
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
        "doc_keywords": "判別ユニオン, switch, 網羅性",
        "doc_notes": "ケース分けの苦労を共有すると盛り上がります。",
        "doc_tone": "バグ修正あるあるテンポ",
        "code": [
            """type Event =
  | { type: "click"; x: number; y: number }
  | { type: "submit"; formId: string };""",
            """function handle(event: Event) {
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
}""",
            """const nowIso = toIso(new Date());

function fromIso(value: IsoDate): Date {
  return new Date(value);
}""",
            """type Timeline = {
  createdAt: IsoDate;
  updatedAt: IsoDate;
};

const timeline: Timeline = { createdAt: nowIso, updatedAt: nowIso };""",
        ],
    },
}


DEFAULT = FEATURES["default"]

for feature in FEATURES.values():
    feature.setdefault("code", DEFAULT["code"])
    feature.setdefault("doc_tone", DEFAULT["doc_tone"])
    feature.setdefault("doc_notes", DEFAULT["doc_notes"])
    feature.setdefault("doc_keywords", DEFAULT["doc_keywords"])
    feature.setdefault("cta_keyword", DEFAULT["cta_keyword"])
    feature.setdefault("empathy", DEFAULT["empathy"])
    feature.setdefault("tech", DEFAULT["tech"])


_KEYWORD_FEATURE_MAP: list[tuple[list[str], str]] = [
    (["any"], "any_escape"),
    (["never", "exhaustive"], "never"),
    (["infer"], "inference"),
    (["as const"], "as_const"),
    (["satisfies"], "satisfies"),
    (["record"], "record"),
    (["deeppartial", "deepreadonly", "partial", "pick", "omit", "dto"], "partial"),
    (["readonlyarray", "readonly", "mutable"], "readonly"),
    (["strictnullchecks", "nullable", "nonnullable", "nounchecked", "unknown", "asserts", "type predicate"], "unknown"),
    (["moduleresolution", "module resolution"], "module"),
    (["esm", "cjs", "import type", "modulesuffixes", "verbatimmodule", "resolvejsonmodule", "module"], "module"),
    (["tsconfig", "noimplicitany", "strict", "extends", "isolatedmodules"], "tsconfig"),
    (["keyof", "generics", "variance", "conditional type", "conditional", "indexed access"], "generics"),
    (["template literal", "keyremap"], "template_literal"),
    (["promise", "awaited", "async", "flatmap", "promiselike"], "async"),
    (["axios", "fetch", "api", "http"], "schema_api"),
    (["zod", "io-ts", "json-schema", "schema", "openapi", "prisma", "drizzle"], "schema"),
    (["interface", "type alias", "構造体", "命名"], "structure"),
    (["decorator", "emitdecoratormetadata"], "decorator"),
    (["react", "jsx", "usestate", "next.js", "react.fc"], "react"),
    (["eslint", "lint", "max-warnings", "prettier", "dprint"], "lint"),
    (["@types", "type-fest", "publishconfig", "tsup", 'types"'], "types_publish"),
    (["workspace", "monorepo", "pnpm", "project references", "yarn workspace"], "orchestration"),
    (["ts-node", "tsc", "ts-loader", "swc", "build", "tsbuildinfo", "ts-jest", "sourcemap", "pretty false"], "tooling"),
    (["result"], "result"),
    (["error"], "error"),
    (["enum"], "enum"),
    (["union"], "union"),
    (["date"], "date"),
]

KEYWORD_FEATURE_MAP: list[tuple[list[str], str]] = [
    ([keyword.lower() for keyword in keywords], feature_id)
    for keywords, feature_id in _KEYWORD_FEATURE_MAP
]


def parse_titles(path: Path) -> list[str]:
    pattern = re.compile(r"^\s*\d+\.\s+「(.+)」")
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


def build_dialogues(title: str, feature: dict[str, object]) -> list[str]:
    cta_keyword = feature["cta_keyword"]
    return [
        f"ずんだもん「TypeScript書いてるとさ、{title}って絶対あるよね？」",
        f"四国めたん「わかります。{feature['empathy']}」",
        f"ずんだもん「しかもそのまま{title}状態になって、チーム全員が固まるんだよ！」",
        f"四国めたん「そこでTypeScriptの{feature['feature_name']}を使えば、{feature['tech']}」",
        f"ずんだもん「いや待って、それやると{title}第2ラウンドが始まるやつ！」",
        f"四国めたん「共感した方は“{cta_keyword}”ってコメントで教えてください！」",
        "ずんだもん「あなたのTypeScriptあるあるも募集中だよ！」",
    ]


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    title_path = base_dir.parent / "aruaru-titles.md"
    daihon_dir = base_dir / "daihon"
    document_dir = base_dir / "document"

    titles = parse_titles(title_path)
    if not titles:
        raise SystemExit("タイトルが見つかりませんでした。")

    daihon_dir.mkdir(parents=True, exist_ok=True)
    document_dir.mkdir(parents=True, exist_ok=True)

    for index, title in enumerate(titles, start=1):
        if index <= 10:
            continue

        feature = choose_feature(title)
        code_snippets = feature["code"]  # type: ignore[assignment]
        code_block = "\n\n".join(code_snippets)  # type: ignore[arg-type]
        dialogues = build_dialogues(title, feature)

        daihon_path = daihon_dir / f"{index:03}.txt"
        document_path = document_dir / f"{index:03}.md"

        daihon_path.write_text("\n".join(dialogues) + "\n", encoding="utf-8")

        doc_lines = [
            f"# #{index:03} 「{title}」制作ドキュメント",
            "",
            "## 台本",
            *dialogues,
            "",
            "## 画面表示用コード",
            "",
            "```typescript",
            code_block,
            "```",
            "",
            "## 制作メモ",
            f"- **想定シーン**: {title}に遭遇した瞬間を切り取るネタ",
            f"- **狙いトーン**: {feature['doc_tone']}",
            f"- **技術キーワード**: {feature['doc_keywords']}",
            f"- **使いたい一言**: 「{feature['cta_keyword']}」",
            f"- **CTA案**: コメントで「{feature['cta_keyword']}」と書いてもらい、同じ経験を募る",
            f"- **備考**: {feature['doc_notes']}",
            "",
        ]

        document_path.write_text("\n".join(doc_lines), encoding="utf-8")


if __name__ == "__main__":
    main()
